from __future__ import annotations

import json
import subprocess

from hexawyn.application.ports.driven.helm_release_version_port import (
    ChartLatestRawData,
    HelmReleaseRawData,
    HelmReleaseVersionPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut: MutantDict = {}  # type: ignore


class HelmReleaseVersionAdapter(HelmReleaseVersionPort):
    @_mutmut_mutated(mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut)
    def list_releases(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_orig(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_1(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = None
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_2(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["XXhelmXX", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_3(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["HELM", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_4(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "XXlistXX", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_5(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "LIST", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_6(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "XX--outputXX", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_7(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--OUTPUT", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_8(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "XXjsonXX"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_9(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "JSON"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_10(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(None)
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_11(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["XX--namespaceXX", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_12(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--NAMESPACE", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_13(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append(None)

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_14(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("XX--all-namespacesXX")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_15(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--ALL-NAMESPACES")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_16(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = None
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_17(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(None, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_18(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=None, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_19(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=None, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_20(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=None)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_21(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_22(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_23(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_24(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, )
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_25(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=False, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_26(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=False, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_27(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=11)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_28(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_29(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 1:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_30(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = None
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_31(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(None)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_32(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = None
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_33(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    None
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_34(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=None,
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_35(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=None,
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_36(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=None,
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_37(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=None,
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_38(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=None,
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_39(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=None,
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_40(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_41(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_42(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_43(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_44(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_45(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_46(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get(None, ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_47(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", None),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_48(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get(""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_49(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_50(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("XXnameXX", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_51(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("NAME", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_52(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", "XXXX"),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_53(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get(None, ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_54(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", None),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_55(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get(""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_56(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_57(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("XXnamespaceXX", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_58(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("NAMESPACE", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_59(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", "XXXX"),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_60(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get(None, ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_61(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", None),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_62(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get(""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_63(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_64(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("XXchartXX", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_65(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("CHART", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_66(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", "XXXX"),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_67(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get(None, ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_68(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", None),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_69(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get(""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_70(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_71(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("XXapp_versionXX", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_72(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("APP_VERSION", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_73(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", "XXXX"),
                        status=release.get("status", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_74(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get(None, ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_75(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", None),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_76(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get(""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_77(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_78(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("XXstatusXX", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_79(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("STATUS", ""),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_80(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", "XXXX"),
                        revision=release.get("revision", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_81(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get(None, 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_82(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", None),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_83(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get(0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_84(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", ),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_85(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("XXrevisionXX", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_86(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("REVISION", 0),
                    )
                )
            return data
        except Exception:
            return []
    def xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_87(self, namespace: str | None) -> list[HelmReleaseRawData]:
        try:
            cmd = ["helm", "list", "--output", "json"]
            if namespace:
                cmd.extend(["--namespace", namespace])
            else:
                cmd.append("--all-namespaces")

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return []

            releases = json.loads(result.stdout)
            data: list[HelmReleaseRawData] = []
            for release in releases:
                data.append(
                    HelmReleaseRawData(  # type: ignore
                        name=release.get("name", ""),
                        namespace=release.get("namespace", ""),
                        chart=release.get("chart", ""),
                        app_version=release.get("app_version", ""),
                        status=release.get("status", ""),
                        revision=release.get("revision", 1),
                    )
                )
            return data
        except Exception:
            return []

    @_mutmut_mutated(mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut)
    def fetch_latest_version(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_orig(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_1(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = None
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_2(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                None,
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_3(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=None,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_4(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=None,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_5(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=None,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_6(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_7(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_8(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_9(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_10(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["XXhelmXX", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_11(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["HELM", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_12(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "XXsearchXX", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_13(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "SEARCH", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_14(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "XXrepoXX", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_15(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "REPO", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_16(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "XX--outputXX", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_17(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--OUTPUT", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_18(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "XXjsonXX"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_19(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "JSON"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_20(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=False,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_21(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=False,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_22(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=11,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_23(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_24(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 1:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_25(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=None,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_26(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=None,
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_27(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes=None,
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_28(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error=None,
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_29(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_30(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_31(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_32(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_33(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="XXXX",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_34(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="XXXX",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_35(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="XXXX",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_36(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = None
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_37(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(None)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_38(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=None,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_39(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=None,
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_40(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes=None,
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_41(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error=None,
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_42(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_43(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_44(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_45(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_46(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get(None, ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_47(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", None),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_48(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get(""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_49(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_50(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[1].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_51(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("XXversionXX", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_52(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("VERSION", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_53(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", "XXXX"),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_54(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="XXXX",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_55(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="XXXX",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_56(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=None,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_57(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version=None,
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_58(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes=None,
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_59(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error=None,
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_60(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_61(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_62(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_63(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_64(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="XXXX",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_65(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="XXXX",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_66(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="XXXX",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_67(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=None,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_68(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version=None,
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_69(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes=None,
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_70(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error=None,
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_71(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                latest_version="",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_72(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_73(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_74(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_75(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="XXXX",
                breaking_changes="",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_76(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="XXXX",
                repo_error="",
            )

    def xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_77(self, chart_name: str) -> ChartLatestRawData:
        try:
            result = subprocess.run(
                ["helm", "search", "repo", chart_name, "--output", "json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version="",
                    breaking_changes="",
                    repo_error="",
                )
            results = json.loads(result.stdout)
            if results:
                return ChartLatestRawData(
                    chart_name=chart_name,
                    latest_version=results[0].get("version", ""),
                    breaking_changes="",
                    repo_error="",
                )
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="",
            )
        except Exception:
            return ChartLatestRawData(
                chart_name=chart_name,
                latest_version="",
                breaking_changes="",
                repo_error="XXXX",
            )

mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['_mutmut_orig'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_1'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_2'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_3'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_4'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_5'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_6'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_7'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_8'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_9'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_10'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_11'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_12'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_13'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_14'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_15'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_16'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_17'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_18'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_19'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_20'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_21'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_22'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_23'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_24'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_25'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_26'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_27'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_28'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_29'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_30'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_31'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_32'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_33'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_34'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_35'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_36'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_37'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_38'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_39'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_40'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_41'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_42'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_43'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_44'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_45'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_46'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_47'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_48'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_49'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_50'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_51'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_52'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_53'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_54'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_55'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_56'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_57'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_58'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_59'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_60'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_61'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_62'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_63'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_64'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_65'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_66'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_67'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_67 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_68'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_68 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_69'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_69 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_70'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_70 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_71'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_71 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_72'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_72 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_73'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_73 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_74'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_74 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_75'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_75 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_76'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_76 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_77'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_77 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_78'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_78 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_79'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_79 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_80'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_80 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_81'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_81 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_82'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_82 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_83'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_83 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_84'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_84 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_85'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_85 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_86'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_86 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁlist_releases__mutmut['xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_87'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁlist_releases__mutmut_87 # type: ignore # mutmut generated

mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['_mutmut_orig'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_1'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_2'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_3'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_4'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_5'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_6'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_7'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_8'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_9'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_10'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_11'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_12'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_13'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_14'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_15'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_16'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_17'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_18'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_19'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_20'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_21'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_22'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_23'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_24'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_25'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_26'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_27'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_28'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_29'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_30'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_31'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_32'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_33'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_34'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_35'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_36'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_37'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_38'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_39'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_40'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_41'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_42'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_43'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_44'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_45'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_46'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_47'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_48'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_49'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_50'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_51'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_52'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_53'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_54'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_55'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_56'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_57'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_58'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_59'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_60'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_61'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_62'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_63'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_64'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_65'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_66'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_67'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_67 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_68'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_68 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_69'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_69 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_70'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_70 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_71'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_71 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_72'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_72 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_73'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_73 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_74'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_74 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_75'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_75 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_76'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_76 # type: ignore # mutmut generated
mutants_xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut['xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_77'] = HelmReleaseVersionAdapter.xǁHelmReleaseVersionAdapterǁfetch_latest_version__mutmut_77 # type: ignore # mutmut generated
