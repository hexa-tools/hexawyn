from __future__ import annotations

import subprocess

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut: MutantDict = {}  # type: ignore


class KubernetesResourceYAMLAdapter(ResourceYAMLPort):
    @_mutmut_mutated(mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut)
    def fetch_resource(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_orig(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_1(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = None
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_2(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                None,
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_3(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=None,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_4(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=None,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_5(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=None,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_6(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_7(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_8(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_9(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_10(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "XXkubectlXX",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_11(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "KUBECTL",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_12(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "XXgetXX",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_13(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "GET",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_14(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.upper(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_15(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "XX-nXX",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_16(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-N",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_17(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "XX-oXX",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_18(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-O",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_19(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "XXyamlXX",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_20(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "YAML",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_21(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=False,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_22(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=False,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_23(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=11,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_24(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 or result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_25(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_26(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 1 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_27(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"XXkindXX": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_28(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"KIND": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_29(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "XXnameXX": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_30(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "NAME": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_31(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "XXyamlXX": result.stdout}
            return {}
        except Exception:
            return {}
    def xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_32(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "YAML": result.stdout}
            return {}
        except Exception:
            return {}

    @_mutmut_mutated(mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut)
    def resource_exists(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_orig(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_1(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = None
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_2(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                None,
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_3(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=None,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_4(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=None,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_5(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=None,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_6(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_7(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_8(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_9(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_10(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "XXkubectlXX",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_11(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "KUBECTL",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_12(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "XXgetXX",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_13(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "GET",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_14(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.upper(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_15(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "XX-nXX",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_16(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-N",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_17(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=False,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_18(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=False,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_19(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=11,
            )
            return result.returncode == 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_20(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode != 0
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_21(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 1
        except Exception:
            return False

    def xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_22(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return True

mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['_mutmut_orig'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_1'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_2'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_3'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_4'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_5'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_6'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_7'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_8'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_9'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_10'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_11'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_12'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_13'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_14'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_15'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_16'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_17'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_18'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_19'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_20'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_21'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_22'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_23'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_24'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_25'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_26'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_27'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_28'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_29'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_30'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_31'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut['xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_32'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁfetch_resource__mutmut_32 # type: ignore # mutmut generated

mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['_mutmut_orig'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_1'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_2'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_3'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_4'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_5'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_6'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_7'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_8'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_9'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_10'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_11'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_12'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_13'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_14'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_15'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_16'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_17'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_18'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_19'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_20'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_21'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut['xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_22'] = KubernetesResourceYAMLAdapter.xǁKubernetesResourceYAMLAdapterǁresource_exists__mutmut_22 # type: ignore # mutmut generated
