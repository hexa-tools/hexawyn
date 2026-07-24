from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.certs_detect.command import CertsDetectCommand
from hexawyn.application.use_case.certs_detect.response import CertsDetectResponse


class CertsDetectUseCase:
    def __init__(self, cert_manager_port: CertManagerPort) -> None:
        self._port = cert_manager_port

    def execute(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )
