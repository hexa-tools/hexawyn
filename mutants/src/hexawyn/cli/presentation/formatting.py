from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
    KubernetesStartupStatus,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_app_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_app_version__mutmut)
def app_version() -> str:
    try:
        return version("hexawyn")
    except PackageNotFoundError:
        return "local"


def x_app_version__mutmut_orig() -> str:
    try:
        return version("hexawyn")
    except PackageNotFoundError:
        return "local"


def x_app_version__mutmut_1() -> str:
    try:
        return version(None)
    except PackageNotFoundError:
        return "local"


def x_app_version__mutmut_2() -> str:
    try:
        return version("XXhexawynXX")
    except PackageNotFoundError:
        return "local"


def x_app_version__mutmut_3() -> str:
    try:
        return version("HEXAWYN")
    except PackageNotFoundError:
        return "local"


def x_app_version__mutmut_4() -> str:
    try:
        return version("hexawyn")
    except PackageNotFoundError:
        return "XXlocalXX"


def x_app_version__mutmut_5() -> str:
    try:
        return version("hexawyn")
    except PackageNotFoundError:
        return "LOCAL"

mutants_x_app_version__mutmut['_mutmut_orig'] = x_app_version__mutmut_orig # type: ignore # mutmut generated
mutants_x_app_version__mutmut['x_app_version__mutmut_1'] = x_app_version__mutmut_1 # type: ignore # mutmut generated
mutants_x_app_version__mutmut['x_app_version__mutmut_2'] = x_app_version__mutmut_2 # type: ignore # mutmut generated
mutants_x_app_version__mutmut['x_app_version__mutmut_3'] = x_app_version__mutmut_3 # type: ignore # mutmut generated
mutants_x_app_version__mutmut['x_app_version__mutmut_4'] = x_app_version__mutmut_4 # type: ignore # mutmut generated
mutants_x_app_version__mutmut['x_app_version__mutmut_5'] = x_app_version__mutmut_5 # type: ignore # mutmut generated
mutants_x_compact_project_directory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compact_project_directory__mutmut)
def compact_project_directory() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def x_compact_project_directory__mutmut_orig() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def x_compact_project_directory__mutmut_1() -> str:
    current_directory = None
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def x_compact_project_directory__mutmut_2() -> str:
    current_directory = Path.cwd()
    home_directory = None
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def x_compact_project_directory__mutmut_3() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = None
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def x_compact_project_directory__mutmut_4() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(None)
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def x_compact_project_directory__mutmut_5() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(None)
    return f"~/{relative_directory.as_posix()}"

mutants_x_compact_project_directory__mutmut['_mutmut_orig'] = x_compact_project_directory__mutmut_orig # type: ignore # mutmut generated
mutants_x_compact_project_directory__mutmut['x_compact_project_directory__mutmut_1'] = x_compact_project_directory__mutmut_1 # type: ignore # mutmut generated
mutants_x_compact_project_directory__mutmut['x_compact_project_directory__mutmut_2'] = x_compact_project_directory__mutmut_2 # type: ignore # mutmut generated
mutants_x_compact_project_directory__mutmut['x_compact_project_directory__mutmut_3'] = x_compact_project_directory__mutmut_3 # type: ignore # mutmut generated
mutants_x_compact_project_directory__mutmut['x_compact_project_directory__mutmut_4'] = x_compact_project_directory__mutmut_4 # type: ignore # mutmut generated
mutants_x_compact_project_directory__mutmut['x_compact_project_directory__mutmut_5'] = x_compact_project_directory__mutmut_5 # type: ignore # mutmut generated


def current_context_from(
    contexts: list[KubernetesClusterContext],
) -> KubernetesClusterContext | None:
    for context in contexts:
        if context.is_current:
            return context
    return None
mutants_x_context_list_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_context_list_lines__mutmut)
def context_list_lines(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_orig(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_1(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = None
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_2(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(None)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_3(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = None
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_4(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_5(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "XXunknownXX"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_6(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "UNKNOWN"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_7(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = None
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_8(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "XXboldXX"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_9(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "BOLD"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_10(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("XXXX", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_11(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "XXdimXX")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_12(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "DIM")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_13(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(None)
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_14(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("XXAvailable contexts:XX", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_15(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_16(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("AVAILABLE CONTEXTS:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_17(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "XXboldXX"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_18(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "BOLD"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_19(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = None
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_20(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "XX*XX" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_21(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else "XX XX"
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_22(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append(None)
    return lines


def x_context_list_lines__mutmut_23(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "XXgreenXX" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_24(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "GREEN" if context.is_current else "dim"))
    return lines


def x_context_list_lines__mutmut_25(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "XXdimXX"))
    return lines


def x_context_list_lines__mutmut_26(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "DIM"))
    return lines

mutants_x_context_list_lines__mutmut['_mutmut_orig'] = x_context_list_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_1'] = x_context_list_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_2'] = x_context_list_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_3'] = x_context_list_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_4'] = x_context_list_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_5'] = x_context_list_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_6'] = x_context_list_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_7'] = x_context_list_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_8'] = x_context_list_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_9'] = x_context_list_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_10'] = x_context_list_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_11'] = x_context_list_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_12'] = x_context_list_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_13'] = x_context_list_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_14'] = x_context_list_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_15'] = x_context_list_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_16'] = x_context_list_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_17'] = x_context_list_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_18'] = x_context_list_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_19'] = x_context_list_lines__mutmut_19 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_20'] = x_context_list_lines__mutmut_20 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_21'] = x_context_list_lines__mutmut_21 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_22'] = x_context_list_lines__mutmut_22 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_23'] = x_context_list_lines__mutmut_23 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_24'] = x_context_list_lines__mutmut_24 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_25'] = x_context_list_lines__mutmut_25 # type: ignore # mutmut generated
mutants_x_context_list_lines__mutmut['x_context_list_lines__mutmut_26'] = x_context_list_lines__mutmut_26 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_missing_context_lines__mutmut)
def missing_context_lines(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_orig(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_1(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = None
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_2(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("XX✗ Context not foundXX", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_3(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_4(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ CONTEXT NOT FOUND", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_5(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "XXredXX"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_6(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "RED"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_7(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("XXXX", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_8(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "XXdimXX"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_9(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "DIM"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_10(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("XXAvailable contexts:XX", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_11(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_12(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("AVAILABLE CONTEXTS:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_13(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "XXboldXX")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_14(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "BOLD")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_15(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend(None)
    return lines


def x_missing_context_lines__mutmut_16(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "XXdimXX") for context in contexts)
    return lines


def x_missing_context_lines__mutmut_17(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "DIM") for context in contexts)
    return lines

mutants_x_missing_context_lines__mutmut['_mutmut_orig'] = x_missing_context_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_1'] = x_missing_context_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_2'] = x_missing_context_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_3'] = x_missing_context_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_4'] = x_missing_context_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_5'] = x_missing_context_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_6'] = x_missing_context_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_7'] = x_missing_context_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_8'] = x_missing_context_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_9'] = x_missing_context_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_10'] = x_missing_context_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_11'] = x_missing_context_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_12'] = x_missing_context_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_13'] = x_missing_context_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_14'] = x_missing_context_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_15'] = x_missing_context_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_16'] = x_missing_context_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x_missing_context_lines__mutmut['x_missing_context_lines__mutmut_17'] = x_missing_context_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_startup_status_from_switch__mutmut)
def startup_status_from_switch(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_orig(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_1(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=None,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_2(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=None,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_3(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=None,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_4(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=None,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_5(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=None,
    )


def x_startup_status_from_switch__mutmut_6(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_7(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_8(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_9(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        connection_error=switch_result.connection_error,
    )


def x_startup_status_from_switch__mutmut_10(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        )

mutants_x_startup_status_from_switch__mutmut['_mutmut_orig'] = x_startup_status_from_switch__mutmut_orig # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_1'] = x_startup_status_from_switch__mutmut_1 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_2'] = x_startup_status_from_switch__mutmut_2 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_3'] = x_startup_status_from_switch__mutmut_3 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_4'] = x_startup_status_from_switch__mutmut_4 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_5'] = x_startup_status_from_switch__mutmut_5 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_6'] = x_startup_status_from_switch__mutmut_6 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_7'] = x_startup_status_from_switch__mutmut_7 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_8'] = x_startup_status_from_switch__mutmut_8 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_9'] = x_startup_status_from_switch__mutmut_9 # type: ignore # mutmut generated
mutants_x_startup_status_from_switch__mutmut['x_startup_status_from_switch__mutmut_10'] = x_startup_status_from_switch__mutmut_10 # type: ignore # mutmut generated
mutants_x_context_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_context_line__mutmut)
def context_line(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_orig(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_1(adapter: Any) -> str:
    ctx = None
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_2(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = None
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_3(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get(None, "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_4(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", None)
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_5(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_6(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", )
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_7(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("XXnamespaceXX", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_8(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("NAMESPACE", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_9(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "XXdefaultXX")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_10(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "DEFAULT")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_11(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = None
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_12(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(None, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_13(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, None) else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_14(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr("get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_15(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, ) else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_16(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "XXget_findingsXX") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_17(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "GET_FINDINGS") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_18(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 1
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_19(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = None
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_20(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "XXyellowXX" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_21(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "YELLOW" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_22(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "XXgreenXX"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_23(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "GREEN"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_24(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = None
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_25(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" - ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_26(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("XXsXX" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_27(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("S" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_28(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings == 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_29(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 2 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_30(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "XXXX")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_31(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get(None, '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_32(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', None)}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_33(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_34(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', )}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_35(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('XXnameXX', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_36(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('NAME', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def x_context_line__mutmut_37(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', 'XXXX')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )

mutants_x_context_line__mutmut['_mutmut_orig'] = x_context_line__mutmut_orig # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_1'] = x_context_line__mutmut_1 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_2'] = x_context_line__mutmut_2 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_3'] = x_context_line__mutmut_3 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_4'] = x_context_line__mutmut_4 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_5'] = x_context_line__mutmut_5 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_6'] = x_context_line__mutmut_6 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_7'] = x_context_line__mutmut_7 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_8'] = x_context_line__mutmut_8 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_9'] = x_context_line__mutmut_9 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_10'] = x_context_line__mutmut_10 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_11'] = x_context_line__mutmut_11 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_12'] = x_context_line__mutmut_12 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_13'] = x_context_line__mutmut_13 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_14'] = x_context_line__mutmut_14 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_15'] = x_context_line__mutmut_15 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_16'] = x_context_line__mutmut_16 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_17'] = x_context_line__mutmut_17 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_18'] = x_context_line__mutmut_18 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_19'] = x_context_line__mutmut_19 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_20'] = x_context_line__mutmut_20 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_21'] = x_context_line__mutmut_21 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_22'] = x_context_line__mutmut_22 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_23'] = x_context_line__mutmut_23 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_24'] = x_context_line__mutmut_24 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_25'] = x_context_line__mutmut_25 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_26'] = x_context_line__mutmut_26 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_27'] = x_context_line__mutmut_27 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_28'] = x_context_line__mutmut_28 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_29'] = x_context_line__mutmut_29 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_30'] = x_context_line__mutmut_30 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_31'] = x_context_line__mutmut_31 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_32'] = x_context_line__mutmut_32 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_33'] = x_context_line__mutmut_33 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_34'] = x_context_line__mutmut_34 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_35'] = x_context_line__mutmut_35 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_36'] = x_context_line__mutmut_36 # type: ignore # mutmut generated
mutants_x_context_line__mutmut['x_context_line__mutmut_37'] = x_context_line__mutmut_37 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_connection_line__mutmut)
def connection_line(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_orig(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_1(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None or not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_2(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_3(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_4(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "XX[yellow]⚠ Disconnected[/yellow]XX"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_5(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_6(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[YELLOW]⚠ DISCONNECTED[/YELLOW]"
    return "[green]✓ Connected[/green]"


def x_connection_line__mutmut_7(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "XX[green]✓ Connected[/green]XX"


def x_connection_line__mutmut_8(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ connected[/green]"


def x_connection_line__mutmut_9(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[GREEN]✓ CONNECTED[/GREEN]"

mutants_x_connection_line__mutmut['_mutmut_orig'] = x_connection_line__mutmut_orig # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_1'] = x_connection_line__mutmut_1 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_2'] = x_connection_line__mutmut_2 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_3'] = x_connection_line__mutmut_3 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_4'] = x_connection_line__mutmut_4 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_5'] = x_connection_line__mutmut_5 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_6'] = x_connection_line__mutmut_6 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_7'] = x_connection_line__mutmut_7 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_8'] = x_connection_line__mutmut_8 # type: ignore # mutmut generated
mutants_x_connection_line__mutmut['x_connection_line__mutmut_9'] = x_connection_line__mutmut_9 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_startup_lines__mutmut)
def startup_lines(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_orig(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_1(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None and startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_2(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is not None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_3(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is not None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_4(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = None
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_5(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = None
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_6(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "XX[green]✓[/green] ConnectedXX"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_7(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_8(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[GREEN]✓[/GREEN] CONNECTED"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_9(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "XX[yellow]⚠[/yellow] Unable to connectXX"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_10(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_11(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[YELLOW]⚠[/YELLOW] UNABLE TO CONNECT"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_12(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "XX[green]✓[/green] Kubernetes detectedXX",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_13(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]


def x_startup_lines__mutmut_14(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[GREEN]✓[/GREEN] KUBERNETES DETECTED",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]

mutants_x_startup_lines__mutmut['_mutmut_orig'] = x_startup_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_1'] = x_startup_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_2'] = x_startup_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_3'] = x_startup_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_4'] = x_startup_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_5'] = x_startup_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_6'] = x_startup_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_7'] = x_startup_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_8'] = x_startup_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_9'] = x_startup_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_10'] = x_startup_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_11'] = x_startup_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_12'] = x_startup_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_13'] = x_startup_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_startup_lines__mutmut['x_startup_lines__mutmut_14'] = x_startup_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_format_size__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_size__mutmut)
def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_orig(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_1(size_bytes: int) -> str:
    if size_bytes <= 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_2(size_bytes: int) -> str:
    if size_bytes < 1025:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_3(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes <= 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_4(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1048577:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_5(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes * 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_6(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1025:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_7(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes <= 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_8(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1073741825:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_9(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes * 1_048_576:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_10(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1048577:.1f} MB"
    return f"{size_bytes / 1_073_741_824:.2f} GB"


def x_format_size__mutmut_11(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes * 1_073_741_824:.2f} GB"


def x_format_size__mutmut_12(size_bytes: int) -> str:
    if size_bytes < 1024:  # noqa: PLR2004
        return f"{size_bytes} B"
    if size_bytes < 1_048_576:  # noqa: PLR2004
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1_073_741_824:  # noqa: PLR2004
        return f"{size_bytes / 1_048_576:.1f} MB"
    return f"{size_bytes / 1073741825:.2f} GB"

mutants_x_format_size__mutmut['_mutmut_orig'] = x_format_size__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_1'] = x_format_size__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_2'] = x_format_size__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_3'] = x_format_size__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_4'] = x_format_size__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_5'] = x_format_size__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_6'] = x_format_size__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_7'] = x_format_size__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_8'] = x_format_size__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_9'] = x_format_size__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_10'] = x_format_size__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_11'] = x_format_size__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_size__mutmut['x_format_size__mutmut_12'] = x_format_size__mutmut_12 # type: ignore # mutmut generated
