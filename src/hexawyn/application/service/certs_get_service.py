from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driving.certs_get.certs_get_command import CertsGetCommand
from hexawyn.application.ports.driving.certs_get.certs_get_response import CertsGetResponse
from hexawyn.application.ports.driving.certs_get.certs_get_service_port import CertsGetServicePort


class CertsGetService(CertsGetServicePort):
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port

    def get_cert(self, command: CertsGetCommand) -> CertsGetResponse:
        c = self._port.get_certificate(name=command.name, namespace=command.namespace)
        return CertsGetResponse(
            name=c.name,
            namespace=c.namespace,
            status=c.status.value,
            issuer_name=c.issuer_name,
            issuer_type=c.issuer_type.value,
            dns_names=c.dns_names,
            not_before=c.not_before,
            not_after=c.not_after,
            days_until_expiry=c.days_until_expiry,
            renewal_time=c.renewal_time,
            auto_renew=c.auto_renew,
            message=c.message,
        )
