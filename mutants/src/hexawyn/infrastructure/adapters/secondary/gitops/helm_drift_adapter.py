from __future__ import annotations

import subprocess

import yaml
from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.domain.errors import ComponentNotInstalledError, ManifestRenderError

_HELM_COMMAND_TIMEOUT_SECONDS = 30.0
_NOT_FOUND_HINT = "not found"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmDriftAdapterǁ_run__mutmut: MutantDict = {}  # type: ignore


class HelmDriftAdapter(DriftDetectionPort):
    """Secondary adapter — shells out to the `helm` CLI. Renders desired
    state via `helm get manifest` (the frozen, stored release manifest),
    never `helm template` (which would re-render fresh and bake in a new
    Helm `date`-function timestamp on every call — see plan Context)."""

    @_mutmut_mutated(mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut)
    def render_desired_manifests(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "manifest", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_orig(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "manifest", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_1(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = None
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_2(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(None)
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_3(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["XXgetXX", "manifest", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_4(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["GET", "manifest", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_5(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "XXmanifestXX", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_6(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "MANIFEST", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_7(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "manifest", source, "XX-nXX", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_8(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "manifest", source, "-N", namespace])
        return _parse_multi_doc_yaml(stdout)

    def xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_9(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "manifest", source, "-n", namespace])
        return _parse_multi_doc_yaml(None)

    @_mutmut_mutated(mutants_xǁHelmDriftAdapterǁsource_exists__mutmut)
    def source_exists(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_orig(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_1(self, source: str, namespace: str) -> bool:
        try:
            self._run(None)
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_2(self, source: str, namespace: str) -> bool:
        try:
            self._run(["XXstatusXX", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_3(self, source: str, namespace: str) -> bool:
        try:
            self._run(["STATUS", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_4(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "XX-nXX", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_5(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-N", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_6(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "XX-oXX", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_7(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-O", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_8(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "XXjsonXX"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_9(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "JSON"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_10(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT not in exc.detail.lower():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_11(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.upper():
                return False
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_12(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return True
            raise
        return True

    def xǁHelmDriftAdapterǁsource_exists__mutmut_13(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return False

    @_mutmut_mutated(mutants_xǁHelmDriftAdapterǁ_run__mutmut)
    def _run(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_orig(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_1(self, args: list[str]) -> str:
        command = None
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_2(self, args: list[str]) -> str:
        command = ["XXhelmXX", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_3(self, args: list[str]) -> str:
        command = ["HELM", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_4(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = None
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_5(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                None,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_6(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=None,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_7(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=None,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_8(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=None,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_9(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_10(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_11(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_12(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_13(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=False,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_14(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=False,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_15(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(None, "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_16(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", None) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_17(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_18(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_19(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("XXhelmXX", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_20(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("HELM", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_21(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "XXhttps://helm.sh/docs/intro/install/XX") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_22(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "HTTPS://HELM.SH/DOCS/INTRO/INSTALL/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_23(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=None, detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_24(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail=None
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_25(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_26(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_27(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(None), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_28(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source="XX XX".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_29(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="XXhelm command timed outXX"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_30(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="HELM COMMAND TIMED OUT"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_31(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode == 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_32(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 1:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_33(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=None, detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_34(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=None)
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_35(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_36(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), )
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_37(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(None), detail=result.stderr.strip())
        return result.stdout

    def xǁHelmDriftAdapterǁ_run__mutmut_38(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source="XX XX".join(args), detail=result.stderr.strip())
        return result.stdout

mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['_mutmut_orig'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_1'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_2'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_3'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_4'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_5'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_6'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_7'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_8'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁrender_desired_manifests__mutmut['xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_9'] = HelmDriftAdapter.xǁHelmDriftAdapterǁrender_desired_manifests__mutmut_9 # type: ignore # mutmut generated

mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['_mutmut_orig'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_1'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_2'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_3'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_4'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_5'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_6'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_7'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_8'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_9'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_10'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_11'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_12'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁsource_exists__mutmut['xǁHelmDriftAdapterǁsource_exists__mutmut_13'] = HelmDriftAdapter.xǁHelmDriftAdapterǁsource_exists__mutmut_13 # type: ignore # mutmut generated

mutants_xǁHelmDriftAdapterǁ_run__mutmut['_mutmut_orig'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_1'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_2'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_3'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_4'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_5'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_6'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_7'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_8'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_9'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_10'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_11'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_12'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_13'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_14'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_15'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_16'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_17'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_18'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_19'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_20'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_21'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_22'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_23'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_24'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_25'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_26'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_27'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_28'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_29'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_30'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_31'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_32'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_33'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_34'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_35'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_36'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_37'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHelmDriftAdapterǁ_run__mutmut['xǁHelmDriftAdapterǁ_run__mutmut_38'] = HelmDriftAdapter.xǁHelmDriftAdapterǁ_run__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_multi_doc_yaml__mutmut)
def _parse_multi_doc_yaml(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_orig(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_1(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = None
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_2(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(None):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_3(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_4(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            break
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_5(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = None
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_6(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get(None)
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_7(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("XXkindXX")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_8(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("KIND")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_9(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = None
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_10(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get(None)
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_11(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("XXmetadataXX")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_12(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("METADATA")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_13(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) and not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_14(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_15(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_16(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            break
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_17(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = None
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_18(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get(None)
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_19(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("XXnameXX")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_20(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("NAME")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_21(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_22(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            break
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_23(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = None
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_24(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get(None)
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_25(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("XXnamespaceXX")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_26(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("NAMESPACE")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_27(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            None
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_28(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=None,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_29(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=None,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_30(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=None,
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_31(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=None,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_32(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_33(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_34(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                data=doc,
            )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_35(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                )
        )
    return manifests


def x__parse_multi_doc_yaml__mutmut_36(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "XXXX",
                data=doc,
            )
        )
    return manifests

mutants_x__parse_multi_doc_yaml__mutmut['_mutmut_orig'] = x__parse_multi_doc_yaml__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_1'] = x__parse_multi_doc_yaml__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_2'] = x__parse_multi_doc_yaml__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_3'] = x__parse_multi_doc_yaml__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_4'] = x__parse_multi_doc_yaml__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_5'] = x__parse_multi_doc_yaml__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_6'] = x__parse_multi_doc_yaml__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_7'] = x__parse_multi_doc_yaml__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_8'] = x__parse_multi_doc_yaml__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_9'] = x__parse_multi_doc_yaml__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_10'] = x__parse_multi_doc_yaml__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_11'] = x__parse_multi_doc_yaml__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_12'] = x__parse_multi_doc_yaml__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_13'] = x__parse_multi_doc_yaml__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_14'] = x__parse_multi_doc_yaml__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_15'] = x__parse_multi_doc_yaml__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_16'] = x__parse_multi_doc_yaml__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_17'] = x__parse_multi_doc_yaml__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_18'] = x__parse_multi_doc_yaml__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_19'] = x__parse_multi_doc_yaml__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_20'] = x__parse_multi_doc_yaml__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_21'] = x__parse_multi_doc_yaml__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_22'] = x__parse_multi_doc_yaml__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_23'] = x__parse_multi_doc_yaml__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_24'] = x__parse_multi_doc_yaml__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_25'] = x__parse_multi_doc_yaml__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_26'] = x__parse_multi_doc_yaml__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_27'] = x__parse_multi_doc_yaml__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_28'] = x__parse_multi_doc_yaml__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_29'] = x__parse_multi_doc_yaml__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_30'] = x__parse_multi_doc_yaml__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_31'] = x__parse_multi_doc_yaml__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_32'] = x__parse_multi_doc_yaml__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_33'] = x__parse_multi_doc_yaml__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_34'] = x__parse_multi_doc_yaml__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_35'] = x__parse_multi_doc_yaml__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_multi_doc_yaml__mutmut['x__parse_multi_doc_yaml__mutmut_36'] = x__parse_multi_doc_yaml__mutmut_36 # type: ignore # mutmut generated
