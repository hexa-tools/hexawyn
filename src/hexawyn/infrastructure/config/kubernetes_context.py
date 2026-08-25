import os
from abc import ABC, abstractmethod
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import yaml
from kubernetes import client, config

_CONNECT_TIMEOUT_SECONDS = 2


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


class HexawynContextConfig:
    def __init__(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or Path.home() / ".config" / "hexawyn" / "config.yaml"

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


class FileKubernetesDiscoveryService(DiscoveryService):
    def __init__(
        self,
        home_path: Path | None = None,
        hexawyn_config: HexawynContextConfig | None = None,
    ) -> None:
        self._home_path = home_path or Path.home()
        self._hexawyn_config = hexawyn_config or HexawynContextConfig()

    def discover(self) -> list[ClusterContext]:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        current_context_name = self._read_current_context_name(kubeconfig_paths)
        contexts = self._read_contexts(kubeconfig_paths, current_context_name)
        return contexts

    def current(self) -> ClusterContext | None:
        for context_entry in self.discover():
            if context_entry.is_current:
                return context_entry
        return None

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

    def _resolve_kubeconfig_paths(self) -> list[Path]:
        env_value = os.environ.get("KUBECONFIG")
        if env_value:
            return self._existing_paths(Path(path) for path in env_value.split(os.pathsep) if path)

        standard_path = self._home_path / ".kube" / "config"
        return self._existing_paths([standard_path])

    def _existing_paths(self, candidate_paths: Iterable[Path]) -> list[Path]:
        return [path for path in candidate_paths if path.is_file() and path.stat().st_size > 0]

    def _read_current_context_name(self, kubeconfig_paths: list[Path]) -> str | None:
        for kubeconfig_path in kubeconfig_paths:
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            current_context = kubeconfig_data.get("current-context")
            if isinstance(current_context, str) and current_context:
                return current_context
        return None

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

    def _find_context_kubeconfig_path(self, context_name: str) -> Path | None:
        for kubeconfig_path in self._resolve_kubeconfig_paths():
            kubeconfig_data = self._load_yaml_mapping(kubeconfig_path)
            raw_contexts = kubeconfig_data.get("contexts")
            if self._has_context(raw_contexts, context_name):
                return kubeconfig_path
        return None

    def _has_context(self, raw_contexts: object, context_name: str) -> bool:
        if not isinstance(raw_contexts, list):
            return False
        for raw_context in raw_contexts:
            if not isinstance(raw_context, Mapping):
                continue
            if raw_context.get("name") == context_name:
                return True
        return False

    def _current_from_contexts(self, contexts: list[ClusterContext]) -> ClusterContext | None:
        for context_entry in contexts:
            if context_entry.is_current:
                return context_entry
        return None

    def _find_context(
        self,
        contexts: list[ClusterContext],
        context_name: str,
    ) -> ClusterContext | None:
        for context_entry in contexts:
            if context_entry.name == context_name:
                return context_entry
        return None

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

    def _kubeconfig_loader_path(self) -> str | None:
        kubeconfig_paths = self._resolve_kubeconfig_paths()
        if not kubeconfig_paths:
            return None
        return os.pathsep.join(str(path) for path in kubeconfig_paths)

    def _load_yaml_mapping(self, kubeconfig_path: Path) -> Mapping[object, object]:
        loaded_config: object = yaml.safe_load(kubeconfig_path.read_text(encoding="utf-8"))
        if isinstance(loaded_config, Mapping):
            return loaded_config
        return {}
