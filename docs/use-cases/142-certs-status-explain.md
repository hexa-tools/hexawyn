# Use Case 142 — Certs Status Explain

## Sample Questions

- "Why was the payments-api certificate not renewed?"
- "Explain why this TLS certificate is in failed status"
- "What is causing the certificate to not be ready?"
- "Why is my Let's Encrypt certificate stuck in issuing?"
- "What should I do to fix the renewal failure?"

---

"Explain why a cert-manager certificate failed to renew, is stuck in issuing, or is not ready, and how to fix it" The user asks via certs_status_explain. The flow crosses the hexagonal layers: MCP Tool → CertsStatusExplainUseCase → CertsStatusExplainServicePort (driven port) → secondary adapter (via adapter_factory) → cert_manager infrastructure.

### Flow 1 — Certs Status Explain execution

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as certs_status_explain (MCP Tool)
    participant UC as CertsStatusExplainUseCase
    participant Port as CertsStatusExplainServicePort
    participant Adapter as Adapter (secondary)

    User->>Tool: "Why was the payments-api certificate not renewed?"
    Tool->>UC: execute(CertsStatusExplainCommand)
    UC->>Port: explain(command)
    Port->>Adapter: backend request
    Adapter-->>Port: CertsStatusExplainResponse
    Port-->>UC: CertsStatusExplainResponse
    UC-->>Tool: result
    Tool-->>User: answer
```

## Key Points

- `CertsStatusExplainUseCase` depends only on `CertsStatusExplainServicePort` — never on a cloud SDK.
- Adapter selection is by `adapter_factory`, never hardcoded.
- `{slug}` is registered in `mcp/tools/{slug}.py` and synced to the control-plane cache.

## Related Files

- `src/hexawyn/application/ports/driving/certs_status_explain/certs_status_explain_service_port.py`
- `src/hexawyn/application/use_case/cert_manager/certs_status_explain/certs_status_explain_use_case.py`
- `src/hexawyn/mcp/tools/certs_status_explain.py`

