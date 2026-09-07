from __future__ import annotations

import subprocess
from pathlib import Path

import yaml
from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.domain.errors import ComponentNotInstalledError, ManifestRenderError

_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS = 15.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKustomizeDriftAdapterǁsource_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut: MutantDict = {}  # type: ignore


class KustomizeDriftAdapter(DriftDetectionPort):
    """Secondary adapter — shells out to the `kustomize` CLI. `source` is a
    local overlay directory path (e.g. `overlays/production`) — the overlay
    is inherently "applied" by rendering that exact path."""

    @_mutmut_mutated(mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut)
    def render_desired_manifests(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["build", source])
        return _parse_multi_doc_yaml(stdout)

    def xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_orig(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["build", source])
        return _parse_multi_doc_yaml(stdout)

    def xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_1(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = None
        return _parse_multi_doc_yaml(stdout)

    def xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_2(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(None)
        return _parse_multi_doc_yaml(stdout)

    def xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_3(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["XXbuildXX", source])
        return _parse_multi_doc_yaml(stdout)

    def xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_4(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["BUILD", source])
        return _parse_multi_doc_yaml(stdout)

    def xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_5(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["build", source])
        return _parse_multi_doc_yaml(None)

    @_mutmut_mutated(mutants_xǁKustomizeDriftAdapterǁsource_exists__mutmut)
    def source_exists(self, source: str, namespace: str) -> bool:
        """Kustomize has no release-registry concept, unlike Helm — a plain
        path existence check is the closest equivalent, kept symmetric with
        the shared port for orphan-detection generality."""
        return Path(source).exists()

    def xǁKustomizeDriftAdapterǁsource_exists__mutmut_orig(self, source: str, namespace: str) -> bool:
        """Kustomize has no release-registry concept, unlike Helm — a plain
        path existence check is the closest equivalent, kept symmetric with
        the shared port for orphan-detection generality."""
        return Path(source).exists()

    def xǁKustomizeDriftAdapterǁsource_exists__mutmut_1(self, source: str, namespace: str) -> bool:
        """Kustomize has no release-registry concept, unlike Helm — a plain
        path existence check is the closest equivalent, kept symmetric with
        the shared port for orphan-detection generality."""
        return Path(None).exists()

    @_mutmut_mutated(mutants_xǁKustomizeDriftAdapterǁ_run__mutmut)
    def _run(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_orig(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_1(self, args: list[str]) -> str:
        command = None
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_2(self, args: list[str]) -> str:
        command = ["XXkustomizeXX", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_3(self, args: list[str]) -> str:
        command = ["KUSTOMIZE", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_4(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = None
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_5(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                None,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_6(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=None,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_7(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=None,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_8(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=None,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_9(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_10(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_11(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_12(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_13(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=False,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_14(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=False,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_15(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                None, "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_16(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", None
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_17(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_18(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_19(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "XXkustomizeXX", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_20(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "KUSTOMIZE", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_21(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "XXhttps://kubectl.docs.kubernetes.io/installation/kustomize/XX"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_22(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "HTTPS://KUBECTL.DOCS.KUBERNETES.IO/INSTALLATION/KUSTOMIZE/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_23(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=None, detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_24(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail=None
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_25(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_26(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_27(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(None), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_28(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source="XX XX".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_29(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="XXkustomize command timed outXX"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_30(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="KUSTOMIZE COMMAND TIMED OUT"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_31(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode == 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_32(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 1:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_33(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=None, detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_34(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=None)
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_35(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_36(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), )
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_37(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(None), detail=result.stderr.strip())
        return result.stdout

    def xǁKustomizeDriftAdapterǁ_run__mutmut_38(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError(
                "kustomize", "https://kubectl.docs.kubernetes.io/installation/kustomize/"
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source="XX XX".join(args), detail=result.stderr.strip())
        return result.stdout

mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut['_mutmut_orig'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut['xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_1'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut['xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_2'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut['xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_3'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut['xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_4'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut['xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_5'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁrender_desired_manifests__mutmut_5 # type: ignore # mutmut generated

mutants_xǁKustomizeDriftAdapterǁsource_exists__mutmut['_mutmut_orig'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁsource_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁsource_exists__mutmut['xǁKustomizeDriftAdapterǁsource_exists__mutmut_1'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁsource_exists__mutmut_1 # type: ignore # mutmut generated

mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['_mutmut_orig'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_1'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_2'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_3'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_4'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_5'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_6'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_7'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_8'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_9'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_10'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_11'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_12'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_13'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_14'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_15'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_16'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_17'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_18'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_19'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_20'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_21'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_22'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_23'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_24'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_25'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_26'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_27'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_28'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_29'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_30'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_31'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_32'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_33'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_34'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_35'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_36'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_37'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKustomizeDriftAdapterǁ_run__mutmut['xǁKustomizeDriftAdapterǁ_run__mutmut_38'] = KustomizeDriftAdapter.xǁKustomizeDriftAdapterǁ_run__mutmut_38 # type: ignore # mutmut generated
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
