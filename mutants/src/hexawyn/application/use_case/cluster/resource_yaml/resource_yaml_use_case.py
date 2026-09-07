from __future__ import annotations

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.application.use_case.cluster.resource_yaml.command import (
    ResourceYamlCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.response import (
    ResourceYamlResponse,
)
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest, ResourceYAMLResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁResourceYAMLUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ResourceYAMLUseCase:
    @_mutmut_mutated(mutants_xǁResourceYAMLUseCaseǁ__init____mutmut)
    def __init__(self, port: ResourceYAMLPort) -> None:
        self._port = port
    def xǁResourceYAMLUseCaseǁ__init____mutmut_orig(self, port: ResourceYAMLPort) -> None:
        self._port = port
    def xǁResourceYAMLUseCaseǁ__init____mutmut_1(self, port: ResourceYAMLPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁResourceYAMLUseCaseǁexecute__mutmut)
    def execute(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_orig(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_1(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = None
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_2(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=None, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_3(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=None, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_4(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=None
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_5(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_6(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_7(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_8(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = None
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_9(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(None)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_10(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = None
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_11(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(None) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_12(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = None
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_13(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=None, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_14(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=None, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_15(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=None)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_16(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_17(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_18(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, )
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_19(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=None,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_20(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=None,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_21(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=None,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_22(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=None,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_23(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=None,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_24(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=None,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_25(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=None,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_26(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_27(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_28(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_29(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_30(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_31(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            resource_limits=r.resource_limits,  # type: ignore
        )

    def xǁResourceYAMLUseCaseǁexecute__mutmut_32(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            )

mutants_xǁResourceYAMLUseCaseǁ__init____mutmut['_mutmut_orig'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁ__init____mutmut['xǁResourceYAMLUseCaseǁ__init____mutmut_1'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['_mutmut_orig'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_1'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_2'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_3'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_4'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_5'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_6'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_7'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_8'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_9'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_10'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_11'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_12'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_13'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_14'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_15'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_16'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_17'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_18'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_19'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_20'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_21'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_22'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_23'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_24'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_25'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_26'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_27'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_28'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_29'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_30'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_31'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁResourceYAMLUseCaseǁexecute__mutmut['xǁResourceYAMLUseCaseǁexecute__mutmut_32'] = ResourceYAMLUseCase.xǁResourceYAMLUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
