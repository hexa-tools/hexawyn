import os
from abc import ABC, abstractmethod
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import yaml
from kubernetes import client, config

_CONNECT_TIMEOUT_SECONDS = 2


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ClusterContext:
    name: str
    cluster: str
    namespace: str
    user: str
    is_current: bool


@dataclass(frozen=True)
class KubernetesStartupStatus:
    contexts: list[ClusterContext]
    current_context: ClusterContext | None
    connected: bool
    kubeconfig_paths: list[Path]
    connection_error: str | None = None


@dataclass(frozen=True)
class KubernetesContextSwitchResult:
    contexts: list[ClusterContext]
    current_context: ClusterContext | None
    connected: bool
    switched: bool
    kubeconfig_paths: list[Path]
    connection_error: str | None = None


class DiscoveryService(ABC):
    @abstractmethod
    def discover(self) -> list[ClusterContext]:
        """Discover contexts from kubeconfig sources."""

    @abstractmethod
    def current(self) -> ClusterContext | None:
        """Return Hexawyn preferred context or Kubernetes current context."""
mutants_xǁHexawynContextConfigǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHexawynContextConfigǁsave_context__mutmut: MutantDict = {}  # type: ignore


class HexawynContextConfig:
    @_mutmut_mutated(mutants_xǁHexawynContextConfigǁ__init____mutmut)
    def __init__(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_orig(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_1(self, config_path: Path | None = None) -> None:
        self._config_path = None
    def xǁHexawynContextConfigǁ__init____mutmut_2(self, config_path: Path | None = None) -> None:
        self._config_path = config_path and Path.home() / ".config" / "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_3(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "hexawyn" * "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_4(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" * "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_5(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() * ".config" / "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_6(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / "XX.configXX" / "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_7(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".CONFIG" / "hexawyn" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_8(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "XXhexawynXX" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_9(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "HEXAWYN" / "config.yaml"
    def xǁHexawynContextConfigǁ__init____mutmut_10(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "hexawyn" / "XXconfig.yamlXX"
    def xǁHexawynContextConfigǁ__init____mutmut_11(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "hexawyn" / "CONFIG.YAML"

    @_mutmut_mutated(mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut)
    def load_preferred_context(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_orig(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_1(self) -> str | None:
        if self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_2(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = None
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_3(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(None)
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_4(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding=None))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_5(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="XXutf-8XX"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_6(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="UTF-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_7(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_8(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = None
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_9(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get(None)
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_10(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("XXdefault_contextXX")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_11(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("DEFAULT_CONTEXT")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_12(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) or default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_13(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = None
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_14(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get(None)
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_15(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("XXlast_contextXX")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_16(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("LAST_CONTEXT")
        if isinstance(last_context, str) and last_context:
            return last_context

        return None

    def xǁHexawynContextConfigǁload_preferred_context__mutmut_17(self) -> str | None:
        if not self._config_path.exists():
            return None

        loaded_config: object = yaml.safe_load(self._config_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, Mapping):
            return None

        default_context = loaded_config.get("default_context")
        if isinstance(default_context, str) and default_context:
            return default_context

        last_context = loaded_config.get("last_context")
        if isinstance(last_context, str) or last_context:
            return last_context

        return None

    @_mutmut_mutated(mutants_xǁHexawynContextConfigǁsave_context__mutmut)
    def save_context(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_orig(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_1(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=None, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_2(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=None)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_3(self, context_name: str) -> None:
        self._config_path.parent.mkdir(exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_4(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, )
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_5(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=False, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_6(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=False)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_7(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            None,
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_8(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            None,
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_9(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=None,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_10(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_11(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_12(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            )

    def xǁHexawynContextConfigǁsave_context__mutmut_13(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "XXdefault_contextXX": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_14(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "DEFAULT_CONTEXT": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_15(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "XXlast_contextXX": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_16(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "LAST_CONTEXT": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_17(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open(None, encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_18(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding=None),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_19(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open(encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_20(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", ),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_21(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("XXwXX", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_22(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("W", encoding="utf-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_23(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="XXutf-8XX"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_24(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="UTF-8"),
            sort_keys=True,
        )

    def xǁHexawynContextConfigǁsave_context__mutmut_25(self, context_name: str) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        yaml.safe_dump(
            {
                "default_context": context_name,
                "last_context": context_name,
            },
            self._config_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

mutants_xǁHexawynContextConfigǁ__init____mutmut['_mutmut_orig'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_1'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_2'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_3'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_4'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_5'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_6'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_7'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_8'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_9'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_10'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁ__init____mutmut['xǁHexawynContextConfigǁ__init____mutmut_11'] = HexawynContextConfig.xǁHexawynContextConfigǁ__init____mutmut_11 # type: ignore # mutmut generated

mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['_mutmut_orig'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_1'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_2'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_3'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_4'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_5'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_6'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_7'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_8'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_9'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_10'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_11'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_12'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_13'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_14'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_15'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_16'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁload_preferred_context__mutmut['xǁHexawynContextConfigǁload_preferred_context__mutmut_17'] = HexawynContextConfig.xǁHexawynContextConfigǁload_preferred_context__mutmut_17 # type: ignore # mutmut generated

mutants_xǁHexawynContextConfigǁsave_context__mutmut['_mutmut_orig'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_1'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_2'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_3'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_4'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_5'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_6'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_7'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_8'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_9'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_10'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_11'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_12'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_13'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_14'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_15'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_16'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_17'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_18'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_19'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_20'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_21'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_22'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_23'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_24'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHexawynContextConfigǁsave_context__mutmut['xǁHexawynContextConfigǁsave_context__mutmut_25'] = HexawynContextConfig.xǁHexawynContextConfigǁsave_context__mutmut_25 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut: MutantDict = {}  # type: ignore


class FileKubernetesDiscoveryService(DiscoveryService):
    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut)
    def __init__(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = home_path or Path.home()
        self._hexawyn_config = hexawyn_config or HexawynContextConfig()
    def xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_orig(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = home_path or Path.home()
        self._hexawyn_config = hexawyn_config or HexawynContextConfig()
    def xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_1(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = None
        self._hexawyn_config = hexawyn_config or HexawynContextConfig()
    def xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_2(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = home_path and Path.home()
        self._hexawyn_config = hexawyn_config or HexawynContextConfig()
    def xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_3(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = home_path or Path.home()
        self._hexawyn_config = None
    def xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_4(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = home_path or Path.home()
        self._hexawyn_config = hexawyn_config and HexawynContextConfig()

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut)
    def discover(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(kubeconfig_paths, current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_orig(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(kubeconfig_paths, current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_1(self) -> list[ClusterContext]:
        kubeconfig_paths = None
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(kubeconfig_paths, current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_2(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = None
        contexts = self._read_contexts(kubeconfig_paths, current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_3(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(None)
        contexts = self._read_contexts(kubeconfig_paths, current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_4(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = None
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_5(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(None, current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_6(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(kubeconfig_paths, None)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_7(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(current_context_name)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_8(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(kubeconfig_paths, )
        return contexts

    def current(self) -> ClusterContext | None:
        for context_entry in self.discover():
            if context_entry.is_current:
                return context_entry
        return None

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut)
    def startup_status(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_orig(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_1(self) -> KubernetesStartupStatus:
        contexts = None
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_2(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = None
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_3(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(None)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_4(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is not None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_5(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=None,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_6(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=None,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_7(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=None,
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_8(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error=None,
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_9(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_10(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_11(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_12(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_13(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_14(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=True,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_15(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="XXNo Kubernetes context foundXX",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_16(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="no kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_17(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="NO KUBERNETES CONTEXT FOUND",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_18(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = None
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_19(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(None)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_20(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=None,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_21(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=None,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_22(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=None,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_23(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=None,
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_24(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=None,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_25(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_26(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_27(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_28(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_29(self) -> KubernetesStartupStatus:
        contexts = self.discover()
        current_context = self._current_from_contexts(contexts)
        if current_context is None:
            return KubernetesStartupStatus(
                contexts=contexts,
                current_context=None,
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="No Kubernetes context found",
            )

        connected, connection_error = self._validate_connection(current_context.name)
        return KubernetesStartupStatus(
            contexts=contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            )

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut)
    def switch_context(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_orig(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_1(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = None
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_2(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = None
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_3(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(None, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_4(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, None)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_5(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_6(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, )
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_7(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is not None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_8(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=None,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_9(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=None,
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_10(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=None,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_11(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=None,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_12(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=None,
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_13(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error=None,
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_14(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_15(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_16(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_17(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_18(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_19(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_20(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(None),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_21(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=True,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_22(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=True,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_23(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="XXContext not foundXX",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_24(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_25(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="CONTEXT NOT FOUND",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_26(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(None)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_27(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = None
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_28(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = None
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_29(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(None)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_30(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = None
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_31(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(None)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_32(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=None,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_33(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=None,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_34(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=None,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_35(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=None,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_36(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=None,
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_37(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=None,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_38(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_39(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_40(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_41(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_42(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            connection_error=connection_error,
        )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_43(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=True,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            )

    def xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_44(self, context_name: str) -> KubernetesContextSwitchResult:
        contexts = self.discover()
        selected_context = self._find_context(contexts, context_name)
        if selected_context is None:
            return KubernetesContextSwitchResult(
                contexts=contexts,
                current_context=self._current_from_contexts(contexts),
                connected=False,
                switched=False,
                kubeconfig_paths=self._resolve_kubeconfig_paths(),
                connection_error="Context not found",
            )

        self._set_kubernetes_current_context(selected_context.name)
        refreshed_contexts = self.discover()
        current_context = self._current_from_contexts(refreshed_contexts)
        connected, connection_error = self._validate_connection(selected_context.name)
        return KubernetesContextSwitchResult(
            contexts=refreshed_contexts,
            current_context=current_context,
            connected=connected,
            switched=False,
            kubeconfig_paths=self._resolve_kubeconfig_paths(),
            connection_error=connection_error,
        )

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut)
    def _resolve_kubeconfig_paths(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_orig(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_1(self) -> list[Path]:
        env_value = None
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_2(self) -> list[Path]:
        env_value = os.environ.get(None)
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_3(self) -> list[Path]:
        env_value = os.environ.get("XXKUBECONFIGXX")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_4(self) -> list[Path]:
        env_value = os.environ.get("kubeconfig")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_5(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(None)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_6(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(None) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_7(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(None) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_8(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = None
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_9(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" * "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_10(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path * ".kube" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_11(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / "XX.kubeXX" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_12(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".KUBE" / "config"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_13(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "XXconfigXX"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_14(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "CONFIG"
        return self._existing_paths([standard_path])

    def xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_15(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths(None)

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut)
    def _existing_paths(self, candidate_paths: Iterable[Path]) -> list[Path]:
        return [path for path in candidate_paths if path.is_file() and path.stat().st_size > 0]

    def xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_orig(self, candidate_paths: Iterable[Path]) -> list[Path]:
        return [path for path in candidate_paths if path.is_file() and path.stat().st_size > 0]

    def xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_1(self, candidate_paths: Iterable[Path]) -> list[Path]:
        return [path for path in candidate_paths if path.is_file() or path.stat().st_size > 0]

    def xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_2(self, candidate_paths: Iterable[Path]) -> list[Path]:
        return [path for path in candidate_paths if path.is_file() and path.stat().st_size >= 0]

    def xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_3(self, candidate_paths: Iterable[Path]) -> list[Path]:
        return [path for path in candidate_paths if path.is_file() and path.stat().st_size > 1]

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut)
    def _read_current_context_name(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get("current-context")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_orig(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get("current-context")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_1(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = None
            current_context = kubeconfig_data.get("current-context")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_2(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(None)
            current_context = kubeconfig_data.get("current-context")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_3(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = None
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_4(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get(None)
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_5(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get("XXcurrent-contextXX")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_6(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get("CURRENT-CONTEXT")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_7(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get("current-context")
            if isinstance(current_context, str) or current_context:
                return current_context
        return None

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut)
    def _read_contexts(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_orig(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_1(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = None
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_2(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = None
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_3(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(None)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_4(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = None
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_5(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get(None)
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_6(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("XXcontextsXX")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_7(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("CONTEXTS")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_8(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(None)
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_9(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(None, current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_10(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, None))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_11(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(current_context_name))
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_12(
        self,
        kubeconfig_paths: list[Path],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if isinstance(raw_contexts, list):
                contexts.extend(self._parse_contexts(raw_contexts, ))
        return contexts

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut)
    def _parse_contexts(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_orig(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_1(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = None
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_2(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_3(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                break
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_4(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = None
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_5(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get(None)
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_6(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("XXnameXX")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_7(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("NAME")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_8(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = None
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_9(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get(None)
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_10(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("XXcontextXX")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_11(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("CONTEXT")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_12(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) and not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_13(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_14(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_15(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                break
            contexts.append(
                self._build_context(context_name, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_16(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                None
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_17(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(None, context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_18(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, None, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_19(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, None)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_20(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_details, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_21(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, current_context_name)
            )
        return contexts

    def xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_22(
        self,
        raw_contexts: list[object],
        current_context_name: str | None,
    ) -> list[ClusterContext]:
        contexts: list[ClusterContext] = []
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            context_name = raw_context.get("name")
            context_details = raw_context.get("context")
            if not isinstance(context_name, str) or not isinstance(context_details, Mapping):
                continue
            contexts.append(
                self._build_context(context_name, context_details, )
            )
        return contexts

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut)
    def _build_context(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_orig(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_1(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = None
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_2(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get(None)
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_3(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("XXclusterXX")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_4(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("CLUSTER")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_5(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = None
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_6(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get(None)
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_7(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("XXnamespaceXX")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_8(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("NAMESPACE")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_9(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = None
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_10(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get(None)
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_11(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("XXuserXX")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_12(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("USER")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_13(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=None,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_14(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=None,
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_15(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=None,
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_16(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=None,
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_17(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=None,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_18(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_19(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_20(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_21(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_22(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_23(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "XXunknownXX",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_24(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "UNKNOWN",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_25(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "XXdefaultXX",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_26(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "DEFAULT",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_27(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "XXunknownXX",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_28(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "UNKNOWN",
            is_current=context_name == current_context_name,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_29(
        self,
        context_name: str,
        context_details: Mapping[object, object],
        current_context_name: str | None,
    ) -> ClusterContext:
        cluster_name = context_details.get("cluster")
        namespace = context_details.get("namespace")
        user_name = context_details.get("user")
        return ClusterContext(
            name=context_name,
            cluster=cluster_name if isinstance(cluster_name, str) else "unknown",
            namespace=namespace if isinstance(namespace, str) else "default",
            user=user_name if isinstance(user_name, str) else "unknown",
            is_current=context_name != current_context_name,
        )

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut)
    def _set_kubernetes_current_context(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_orig(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_1(self, context_name: str) -> None:
        kubeconfig_path = None
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_2(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(None)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_3(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is not None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_4(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = None
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_5(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(None)
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_6(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding=None))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_7(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="XXutf-8XX"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_8(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="UTF-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_9(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_10(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = None
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_11(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(None, loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_12(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], None)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_13(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_14(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], )
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_15(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = None
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_16(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["XXcurrent-contextXX"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_17(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["CURRENT-CONTEXT"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_18(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            None,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_19(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            None,
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_20(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=None,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_21(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_22(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_23(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_24(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open(None, encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_25(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding=None),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_26(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open(encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_27(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", ),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_28(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("XXwXX", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_29(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("W", encoding="utf-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_30(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="XXutf-8XX"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_31(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="UTF-8"),
            sort_keys=False,
        )

    def xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_32(self, context_name: str) -> None:
        kubeconfig_path = self._find_context_kubeconfig_path(context_name)
        if kubeconfig_path is None:
            return

        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if not isinstance(loaded_config, dict):
            return

        kubeconfig_data = cast(dict[object, object], loaded_config)
        kubeconfig_data["current-context"] = context_name
        yaml.safe_dump(
            kubeconfig_data,
            kubeconfig_path.open("w", encoding="utf-8"),
            sort_keys=True,
        )

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut)
    def _find_context_kubeconfig_path(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_orig(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_1(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = None
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_2(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(None)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_3(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = None
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_4(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get(None)
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_5(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("XXcontextsXX")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_6(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("CONTEXTS")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_7(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(None, context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_8(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, None):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_9(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(context_name):
                return kubeconfig_path
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_10(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, ):
                return kubeconfig_path
        return None

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut)
    def _has_context(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_orig(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_1(self, raw_contexts: object, context_name: str) -> bool:
        if isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_2(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return True
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_3(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_4(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                break
            if raw_context.get("name") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_5(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get(None) == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_6(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("XXnameXX") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_7(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("NAME") == context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_8(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") != context_name:
                return True
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_9(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return False
        return False

    def xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_10(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return True

    def _current_from_contexts(self, contexts: list[ClusterContext]) -> ClusterContext | None:
        for context_entry in contexts:
            if context_entry.is_current:
                return context_entry
        return None

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut)
    def _find_context(
        self,
        contexts: list[ClusterContext],
        context_name: str,
    ) -> ClusterContext | None:
        for context_entry in contexts:
            if context_entry.name == context_name:
                return context_entry
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut_orig(
        self,
        contexts: list[ClusterContext],
        context_name: str,
    ) -> ClusterContext | None:
        for context_entry in contexts:
            if context_entry.name == context_name:
                return context_entry
        return None

    def xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut_1(
        self,
        contexts: list[ClusterContext],
        context_name: str,
    ) -> ClusterContext | None:
        for context_entry in contexts:
            if context_entry.name != context_name:
                return context_entry
        return None

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut)
    def _validate_connection(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_orig(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_1(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = None
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_2(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=None,
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_3(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=None,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_4(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=None,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_5(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_6(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_7(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_8(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = None
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_9(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=None)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_10(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=None
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_11(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=None).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_12(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return False, None
        except Exception as exc:
            return False, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_13(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return True, str(exc)

    def xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_14(self, context_name: str) -> tuple[bool, str | None]:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=self._kubeconfig_loader_path(),
                context=context_name,
                client_configuration=cfg,
            )
            api_client = client.ApiClient(configuration=cfg)
            client.VersionApi(api_client=api_client).get_code(
                _request_timeout=_CONNECT_TIMEOUT_SECONDS
            )
            return True, None
        except Exception as exc:
            return False, str(None)

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut)
    def _kubeconfig_loader_path(self) -> str | None:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        if not kubeconfig_paths:
            return None
        return os.pathsep.join(str(path) for path in kubeconfig_paths)

    def xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_orig(self) -> str | None:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        if not kubeconfig_paths:
            return None
        return os.pathsep.join(str(path) for path in kubeconfig_paths)

    def xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_1(self) -> str | None:
        kubeconfig_paths = None
        if not kubeconfig_paths:
            return None
        return os.pathsep.join(str(path) for path in kubeconfig_paths)

    def xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_2(self) -> str | None:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        if kubeconfig_paths:
            return None
        return os.pathsep.join(str(path) for path in kubeconfig_paths)

    def xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_3(self) -> str | None:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        if not kubeconfig_paths:
            return None
        return os.pathsep.join(None)

    def xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_4(self) -> str | None:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        if not kubeconfig_paths:
            return None
        return os.pathsep.join(str(None) for path in kubeconfig_paths)

    @_mutmut_mutated(mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut)
    def _load_yaml_mapping(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

    def xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_orig(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

    def xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_1(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = None
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

    def xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_2(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(None)
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

    def xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_3(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding=None))
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

    def xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_4(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="XXutf-8XX"))
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

    def xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_5(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="UTF-8"))
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}

mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut['xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut['xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut['xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ__init____mutmut['xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut['xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁdiscover__mutmut_8 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_15'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_16'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_17'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_18'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_19'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_20'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_21'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_22'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_23'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_24'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_25'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_26'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_27'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_28'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut['xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_29'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁstartup_status__mutmut_29 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_15'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_16'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_17'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_18'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_19'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_20'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_20 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_21'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_21 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_22'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_22 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_23'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_23 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_24'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_24 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_25'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_25 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_26'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_26 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_27'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_27 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_28'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_28 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_29'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_29 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_30'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_30 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_31'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_31 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_32'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_32 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_33'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_33 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_34'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_34 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_35'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_35 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_36'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_36 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_37'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_37 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_38'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_38 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_39'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_39 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_40'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_40 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_41'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_41 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_42'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_42 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_43'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_43 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut['xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_44'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁswitch_context__mutmut_44 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_14 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_15'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_resolve_kubeconfig_paths__mutmut_15 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut['xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_existing_paths__mutmut_3 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_current_context_name__mutmut_7 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_read_contexts__mutmut_12 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_14 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_15'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_15 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_16'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_16 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_17'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_17 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_18'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_18 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_19'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_19 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_20'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_20 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_21'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_21 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut['xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_22'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_parse_contexts__mutmut_22 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_15'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_16'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_17'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_18'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_19'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_20'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_20 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_21'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_21 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_22'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_22 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_23'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_23 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_24'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_24 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_25'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_25 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_26'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_26 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_27'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_27 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_28'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_28 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_29'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_build_context__mutmut_29 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_15'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_16'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_17'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_18'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_19'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_20'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_20 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_21'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_21 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_22'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_22 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_23'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_23 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_24'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_24 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_25'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_25 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_26'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_26 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_27'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_27 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_28'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_28 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_29'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_29 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_30'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_30 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_31'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_31 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_32'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_set_kubernetes_current_context__mutmut_32 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context_kubeconfig_path__mutmut_10 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_has_context__mutmut_10 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut['xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_find_context__mutmut_1 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_6'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_7'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_8'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_9'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_10'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_11'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_11 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_12'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_12 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_13'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_13 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut['xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_14'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_validate_connection__mutmut_14 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut['xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_kubeconfig_loader_path__mutmut_4 # type: ignore # mutmut generated

mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut['_mutmut_orig'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut['xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_1'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut['xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_2'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut['xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_3'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut['xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_4'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut['xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_5'] = FileKubernetesDiscoveryService.xǁFileKubernetesDiscoveryServiceǁ_load_yaml_mapping__mutmut_5 # type: ignore # mutmut generated
