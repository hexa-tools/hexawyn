from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cert_manager.certs_challenges_list.certs_challenges_list_use_case import (  # noqa: E501
    CertsChallengesListUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_challenges_list.command import (
    CertsChallengesListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_detect.certs_detect_use_case import (
    CertsDetectUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_detect.command import CertsDetectCommand
from hexawyn.application.use_case.cert_manager.certs_get.certs_get_use_case import CertsGetUseCase
from hexawyn.application.use_case.cert_manager.certs_get.command import CertsGetCommand
from hexawyn.application.use_case.cert_manager.certs_issuer_get.certs_issuer_get_use_case import (
    CertsIssuerGetUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_issuer_get.command import CertsIssuerGetCommand
from hexawyn.application.use_case.cert_manager.certs_issuers_list.certs_issuers_list_use_case import (  # noqa: E501
    CertsIssuersListUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_issuers_list.command import (
    CertsIssuersListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_list.certs_list_use_case import (
    CertsListUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_list.command import CertsListCommand
from hexawyn.application.use_case.cert_manager.certs_requests_list.certs_requests_list_use_case import (  # noqa: E501
    CertsRequestsListUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_requests_list.command import (
    CertsRequestsListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_status_explain.certs_status_explain_use_case import (  # noqa: E501
    CertsStatusExplainUseCase,
)
from hexawyn.application.use_case.cert_manager.certs_status_explain.command import (
    CertsStatusExplainCommand,
)


class TestCertsUseCases:
    def test_certs_list(self) -> None:
        p = MagicMock()
        p.list_certificates.return_value = []
        result = CertsListUseCase(p).execute(CertsListCommand())
        assert result is not None

    def test_certs_get(self) -> None:
        p = MagicMock()
        m = MagicMock()
        m.name = "cert-1"
        m.namespace = "default"
        m.status = MagicMock()
        m.status.value = "Ready"
        m.issuer_name = "i"
        m.issuer_type = MagicMock()
        m.issuer_type.value = "CI"
        m.dns_names = []
        m.not_before = "a"
        m.not_after = "b"
        m.days_until_expiry = 1
        m.renewal_time = "c"
        m.auto_renew = True
        m.message = "ok"
        p.get_certificate.return_value = m
        result = CertsGetUseCase(p).execute(CertsGetCommand(name="c", namespace="n"))
        assert result.name == "cert-1"

    def test_certs_detect(self) -> None:
        p = MagicMock()
        m = MagicMock()
        m.installed = True
        m.version = "v1"
        m.namespace = "ns"
        m.total_certs = 5
        m.ready_certs = 4
        m.expiring_soon = 1
        m.failed_certs = 0
        m.active_challenges = 0
        p.detect.return_value = m
        result = CertsDetectUseCase(p).execute(CertsDetectCommand())
        assert result.installed is True

    def test_certs_issuer_get(self) -> None:
        p = MagicMock()
        m = MagicMock()
        m.name = "letsencrypt"
        m.namespace = "n"
        m.kind = MagicMock()
        m.kind.value = "CI"
        m.status = MagicMock()
        m.status.value = "Ready"
        m.ready = True
        m.server = "s"
        m.message = "ok"
        p.get_issuer.return_value = m
        result = CertsIssuerGetUseCase(p).execute(CertsIssuerGetCommand(name="l", namespace="n"))
        assert result.name == "letsencrypt"

    def test_certs_issuers_list(self) -> None:
        p = MagicMock()
        p.list_issuers.return_value = []
        assert CertsIssuersListUseCase(p).execute(CertsIssuersListCommand()) is not None

    def test_certs_requests_list(self) -> None:
        p = MagicMock()
        p.list_requests.return_value = []
        assert CertsRequestsListUseCase(p).execute(CertsRequestsListCommand()) is not None

    def test_certs_challenges_list(self) -> None:
        p = MagicMock()
        p.list_challenges.return_value = []
        assert CertsChallengesListUseCase(p).execute(CertsChallengesListCommand()) is not None

    def test_certs_status_explain(self) -> None:
        p = MagicMock()
        m = MagicMock()
        m.name = "cert-1"
        m.namespace = "n"
        m.status = MagicMock()
        m.status.value = "Ready"
        m.message = "ok"
        p.get_certificate.return_value = m
        result = CertsStatusExplainUseCase(p).execute(
            CertsStatusExplainCommand(name="c", namespace="n")
        )
        assert result is not None
