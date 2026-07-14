# Use Case 17 — Check Cluster Certificate Health

## Sample Questions

- "Which TLS certificates in the cluster are expiring soon?"
- "Are any certificates going to expire in the next 7 days?"
- "Show me all expired certificates across all namespaces"
- "Which TLS secrets are not referenced by any ingress — orphaned certs?"
- "Is cert-manager managing the renewal of my production certificates?"

---

## Happy Path

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant UC as CheckClusterCertificateHealthUseCase
    participant Svc as ClusterCertificateHealthService
    participant Port as ClusterCertificateHealthPort (ABC)
    participant Adapter as KubernetesClusterCertificateAdapter
    participant K8s as Kubernetes API

    User->>MCP: check_cluster_certificate_health(warning_days=30, critical_days=7)
    MCP->>UC: execute(CheckClusterCertificateHealthCommand)
    UC->>Svc: check_cluster_certificate_health(command)

    Svc->>Port: list_namespaces()
    Port->>Adapter: list_namespaces()
    Adapter->>K8s: CoreV1Api.list_namespace(timeout_seconds=10)
    K8s-->>Adapter: NamespaceList
    Adapter-->>Svc: ["default", "production", "monitoring"]

    loop Each namespace
        Svc->>Port: list_tls_secrets(namespace)
        Port->>Adapter: list_tls_secrets(namespace)
        Adapter->>K8s: list_namespaced_secret(type="kubernetes.io/tls")
        K8s-->>Adapter: SecretList
        Note over Adapter: base64-decode tls.crt<br/>Check cert-manager annotation<br/>Call CustomObjectsApi for renewal status
        Adapter-->>Svc: [TlsSecretData]

        Svc->>Port: list_ingresses(namespace)
        Port->>Adapter: list_ingresses(namespace)
        Adapter->>K8s: NetworkingV1Api.list_namespaced_ingress()
        K8s-->>Adapter: IngressList
        Adapter-->>Svc: [IngressRef]

        Note over Svc: _build_ingress_map() → {secret_name: [ingress_names]}<br/>_parse_pem_to_cert_info() → X.509 parse via cryptography lib<br/>CertificateChecker.check() → status (CRITICAL/WARNING/HEALTHY/EXPIRED)<br/>is_orphan = len(ingress_refs) == 0<br/>is_wildcard = CN starts with "*." or any SAN starts with "*."
    end

    Note over Svc: _build_report() → sort by days_remaining<br/>critical (≤7d) · warning (≤30d) · healthy (>30d) · expired (<0d)
    Svc-->>UC: CheckClusterCertificateHealthResponse
    UC-->>MCP: response.report
    MCP-->>User: {critical, warning, healthy, expired, skipped_namespaces, total_scanned}
```

---

## Error Flows

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant Svc as ClusterCertificateHealthService
    participant Adapter as KubernetesClusterCertificateAdapter
    participant K8s as Kubernetes API

    User->>MCP: check_cluster_certificate_health()

    alt Namespace listing fails (cluster unreachable)
        Adapter->>K8s: list_namespace()
        K8s--xAdapter: ConnectionError / timeout
        Adapter-->>Svc: AdapterTimeoutError
        Svc-->>MCP: AdapterTimeoutError propagates
        MCP-->>User: {error: "AdapterTimeoutError: ...", total_scanned: 0}

    else RBAC denied for a namespace (403 Forbidden)
        Adapter->>K8s: list_namespaced_secret("restricted")
        K8s--xAdapter: ApiException(status=403)
        Adapter-->>Svc: InsufficientPermissionsError
        Note over Svc: Caught per-namespace → namespace added to skipped_namespaces<br/>Scan continues in remaining namespaces
        Svc-->>MCP: ClusterCertificateReport(skipped_namespaces=["restricted"])
        MCP-->>User: {skipped_namespaces: ["restricted"], ...}

    else Invalid PEM in a TLS secret
        Note over Svc: cryptography.load_pem_x509_certificate raises ValueError
        Note over Svc: Caught per-secret → secret silently skipped<br/>total_scanned not incremented for that secret
        Svc-->>MCP: ClusterCertificateReport (partial)
        MCP-->>User: {total_scanned: N-1, ...}

    else cert-manager CRD not installed
        Note over Adapter: CustomObjectsApi.get_namespaced_custom_object raises
        Note over Adapter: Exception swallowed → cert_manager_auto_renewing=False
        Adapter-->>Svc: TlsSecretData(cert_manager_auto_renewing=False)
    end
```

---

## Checker Node — Response Quality Validation

```mermaid
sequenceDiagram
    participant Tool as MCP Tool
    participant Gen as generate_response (LLM)
    participant CK as checker_node
    participant Mem as store_memory
    participant Fmt as format_response

    Tool-->>Gen: ClusterCertificateReport (raw data)
    Gen-->>CK: LLM-generated summary of certificate health

    alt PASS — coherent summary, critical certs highlighted
        CK->>Mem: store_memory(query, result, cluster)
        Mem-->>Fmt: stored
        CK-->>Fmt: status=PASS
        Fmt-->>User: certificate health summary

    else FAIL (attempt < 3) — missing critical certs or wrong days
        CK-->>Gen: retry with corrected prompt
        Note over CK,Gen: retry_count += 1<br/>checker hints: "you missed 2 CRITICAL certs"
        Gen-->>CK: revised summary

    else FAIL (attempt ≥ 3) — DEGRADED
        CK-->>Fmt: status=DEGRADED
        Fmt-->>User: raw report data + "summary generation failed"

    else BLOCKED — mutation detected in response
        Note over CK: Response contains "delete", "drain", "scale replicas=0"
        CK-->>Fmt: status=BLOCKED
        Fmt-->>User: "Operation blocked — read-only tool"

    else FLAG — partial data (skipped namespaces)
        Note over CK: skipped_namespaces not empty → incomplete scan
        CK->>Mem: store_memory(with flag metadata)
        CK-->>Fmt: status=FLAG, caveats=["restricted namespace skipped"]
        Fmt-->>User: summary + caveat banner
    end
```

---

## Key Points

- **Per-namespace RBAC resilience** — a single 403 on a namespace adds it to `skipped_namespaces` and the scan continues; no crash, no partial silence.
- **cert-manager auto-renewal detection** — the adapter checks the Certificate CR status via `CustomObjectsApi`; `Ready=False` means a renewal is in flight; exceptions are swallowed so non-cert-manager clusters work unchanged.
- **Orphan detection** — `is_orphan=True` when no Ingress references the secret, helping clean up abandoned TLS secrets.
- **Wildcard detection** — CN or any SAN starting with `*.` sets `is_wildcard=True` on the entry.
- **Sorted buckets** — critical/warning/healthy/expired each sorted ascending by `days_remaining` so the most urgent certificates appear first.

## Test Coverage

| Test | Scenario |
|------|----------|
| `TestCheckClusterCertificateHealthCommand::test_defaults` | Default thresholds (30d/7d/10s) |
| `TestCheckClusterCertificateHealthCommand::test_is_frozen` | Command is immutable |
| `TestClusterCertificateHealthService::test_happy_path_healthy_cert` | Single healthy cert → 1 in healthy bucket |
| `TestClusterCertificateHealthService::test_critical_cert_classified_correctly` | 3d remaining → CRITICAL |
| `TestClusterCertificateHealthService::test_warning_cert_classified_correctly` | 20d remaining → WARNING |
| `TestClusterCertificateHealthService::test_expired_cert_classified_correctly` | -5d → EXPIRED |
| `TestClusterCertificateHealthService::test_cert_with_ingress_ref_not_orphan` | Ingress references secret → is_orphan=False |
| `TestClusterCertificateHealthService::test_cert_without_ingress_ref_is_orphan` | No ingress → is_orphan=True |
| `TestClusterCertificateHealthService::test_rbac_blocked_namespace_skipped` | 403 namespace → skipped_namespaces populated |
| `TestKubernetesAdapterHelpers::test_list_tls_secrets_rbac_403_raises` | RBAC 403 → InsufficientPermissionsError |
| `TestKubernetesAdapterHelpers::test_list_tls_secrets_non_403_error_reraises` | Non-403 exception → re-raised |
| `TestKubernetesAdapterHelpers::test_is_auto_renewing_cert_not_ready_returns_true` | CR Ready=False → auto_renewing=True |
| `TestKubernetesAdapterHelpers::test_is_auto_renewing_api_error_returns_false` | CRD not installed → False (no crash) |
| `TestParsePemToCertInfo::test_cert_with_san_extension_populates_san_list` | SAN extension parsed correctly |
| `TestCheckClusterCertificateHealthMCPTool::test_tool_error_returns_error_key` | Exception → error key in result |

## Related Files

- `src/hexawyn/domain/models/certificate.py` — `CertificateEntry`, `ClusterCertificateReport`, `CertificateInfo`
- `src/hexawyn/domain/services/certificate/checker.py` — `CertificateChecker` (EXPIRED/CRITICAL/WARNING/HEALTHY)
- `src/hexawyn/application/ports/driven/cluster_certificate_health_port.py` — `ClusterCertificateHealthPort` ABC, `TlsSecretData`, `IngressRef`
- `src/hexawyn/application/ports/driving/check_cluster_certificate_health/` — command, response, service port ABC
- `src/hexawyn/application/service/cluster_certificate_health_service.py` — full service with PEM parsing + report building
- `src/hexawyn/application/use_case/check_cluster_certificate_health/check_cluster_certificate_health_use_case.py` — thin use case
- `src/hexawyn/adapters/secondary/kubernetes_cluster_certificate_adapter.py` — K8s adapter (secrets, ingresses, cert-manager CR)
- `src/hexawyn/mcp/tools/check_cluster_certificate_health.py` — MCP tool registration + serialization
- `tests/unit/test_check_cluster_certificate_health_use_case.py` — 69 unit tests
