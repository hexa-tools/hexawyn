"""MCP client integration abstraction — external coding agent configuration.

Each integration configures an external coding agent (Claude Code, OpenCode,
...) to consume the existing Hexawyn MCP server. This lives outside the
Hexawyn diagnostic core: integrations only translate MCP client configuration
into external CLI calls, keeping the diagnostic engine decoupled from any
coding agent.
"""

from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

MCP_SERVER_NAME = "hexawyn"
MCP_TRANSPORT = "stdio"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str = ""


class CommandRunner(Protocol):
    def run(self, command: list[str]) -> CommandResult:
        """Execute a command and return its captured result."""
mutants_xǁSubprocessRunnerǁrun__mutmut: MutantDict = {}  # type: ignore


class SubprocessRunner:
    """CommandRunner implementation backed by subprocess."""

    @_mutmut_mutated(mutants_xǁSubprocessRunnerǁrun__mutmut)
    def run(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_orig(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_1(self, command: list[str]) -> CommandResult:
        try:
            proc = None
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_2(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(None, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_3(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=None, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_4(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=None, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_5(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=None)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_6(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_7(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_8(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_9(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, )
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_10(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=False, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_11(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=False, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_12(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=31)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_13(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=None, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_14(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout=None, stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_15(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=None)
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_16(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_17(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_18(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", )
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_19(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=128, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_20(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="XXXX", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_21(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(None))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_22(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=None, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_23(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout=None, stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_24(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=None)
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_25(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_26(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_27(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", )
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_28(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=125, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_29(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="XXXX", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_30(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(None))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_31(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=None, stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_32(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=None, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_33(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=None)

    def xǁSubprocessRunnerǁrun__mutmut_34(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(stdout=proc.stdout, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_35(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stderr=proc.stderr)

    def xǁSubprocessRunnerǁrun__mutmut_36(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, )

mutants_xǁSubprocessRunnerǁrun__mutmut['_mutmut_orig'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_1'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_2'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_3'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_4'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_5'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_6'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_7'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_8'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_9'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_10'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_11'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_12'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_13'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_14'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_15'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_16'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_17'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_18'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_19'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_20'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_21'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_22'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_23'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_24'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_25'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_26'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_27'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_28'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_29'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_30'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_31'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_32'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_33'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_34'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_35'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSubprocessRunnerǁrun__mutmut['xǁSubprocessRunnerǁrun__mutmut_36'] = SubprocessRunner.xǁSubprocessRunnerǁrun__mutmut_36 # type: ignore # mutmut generated


@dataclass(frozen=True)
class IntegrationStatus:
    configured: bool
    transport: str = MCP_TRANSPORT
    endpoint: str = ""
    command: str = ""
    error: str | None = None


@dataclass(frozen=True)
class IntegrationResult:
    success: bool
    message: str
    already_configured: bool = False


class MCPClientIntegration(ABC):
    """Configure an external coding agent to consume the Hexawyn MCP server."""

    client_name: str = ""

    @abstractmethod
    def is_available(self) -> bool:
        """Return whether the client binary is installed."""

    @abstractmethod
    def is_installed(self) -> bool:
        """Return whether the hexawyn MCP server is already configured."""

    @abstractmethod
    def install(self) -> IntegrationResult:
        """Configure the hexawyn MCP server for the client (idempotent)."""

    @abstractmethod
    def uninstall(self) -> IntegrationResult:
        """Remove only the hexawyn MCP server for the client."""

    @abstractmethod
    def status(self) -> IntegrationStatus:
        """Report whether the hexawyn MCP server is configured for the client."""
