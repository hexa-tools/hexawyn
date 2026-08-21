# Use Case — TLS Certificate Diagnosis

## Sample Questions

- "Diagnose the TLS certificate on the payment-service ingress."
- "Is the ingress certificate expired, misconfigured, or using a deprecated cipher?"
- "Check the TLS certificate validity and SANs for the production ingress."
- "Why is the checkout ingress returning SSL handshake errors?"

---

Diagnoses the TLS certificate backing an Ingress through: MCP Tool →
TLSCertificateDiagnosisUseCase → ClusterCertificateHealthPort →
KubernetesClusterCertificateAdapter → Kubernetes Networking/Secrets API.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as tls_certificate_diagnosis()
    participant UseCase as TLSCertificateDiagnosisUseCase
    participant Port as ClusterCertificateHealthPort (ABC)
    participant Adapter as KubernetesClusterCertificateAdapter
    participant API as K8s Secrets + Ingress API

    AI->>Tool: Call "tls_certificate_diagnosis" (ingress_name, namespace)
    Tool->>UseCase: use_case(port=build_k8s_adapter()).execute(command)
    UseCase->>Port: list_ingresses(namespace) + list_tls_secrets(namespace)
    Port->>Adapter: map ingress → TLS secret
    Adapter->>API: read ingress + secret
    API-->>Adapter: secret (tls.crt)
    Adapter-->>Port: IngressRef + TlsSecretData
    Port-->>UseCase: certificate data
    UseCase-->>Tool: diagnosis (expiry, SANs, cipher)
    Tool-->>AI: verdict
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as tls_certificate_diagnosis()
    participant Adapter as KubernetesClusterCertificateAdapter

    Tool->>Adapter: read ingress
    alt RBAC 403
        Adapter-->>Tool: InsufficientPermissionsError
    else secret/ingress missing
        Adapter-->>Tool: ResourceNotFoundError
    end
    Tool-->>Tool: { error: "..." }
```

## Key Points

- Maps an Ingress to its TLS secret, parses `tls.crt`, checks expiry/SANs.
- 403 → `InsufficientPermissionsError`, missing resource → `ResourceNotFoundError`.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_returns_response` | `tests/unit/application/use_case/cert_manager/test_uc_tls_certificate_diagnosis_use_case.py` | ✅ |
| `test_parse_pem` | `tests/unit/domain/models/test_tls_certificate_diagnosis.py` | ✅ |
| `test_tool_returns_dict` | `tests/unit/mcp/tools/test_tool_tls_certificate_diagnosis.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/tls_certificate_diagnosis.py`
- `src/hexawyn/application/use_case/cert_manager/tls_certificate_diagnosis/`
- `src/hexawyn/application/ports/driven/cluster_certificate_health_port.py`
- `src/hexawyn/adapters/secondary/kubernetes_cluster_certificate_adapter.py`
