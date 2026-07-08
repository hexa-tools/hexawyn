# Use Case 10 — Resource YAML Definition

## Sample Questions

- "Get the full YAML definition of the deployment order-api in namespace production"
- "What are the current resource limits and image version for the auth-service?"
- "Show me the ConfigMap for the payments service"
- "Get the Secret definition for db-creds (values redacted)"
- "What is the spec of the checkout-service StatefulSet?"

---

One MCP tool: `resource_yaml`. Retrieves full YAML/json definition of k8s resources, extracts image tags and resource limits, redacts Secret values.

### Flow 1 — Happy Path: Deployment with Limits

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as resource_yaml
    participant Service as ResourceYAMLService
    participant Port as ResourceYAMLPort
    participant Adapter as KubernetesResourceYAMLAdapter
    participant K8s as Kubernetes API

    AI->>MCP: "Get YAML of order-api deployment"
    MCP->>Tool: resource_yaml("order-api", "production", "Deployment")

    Tool->>Service: get_resource(command)
    Service->>Port: resource_exists(req)
    Port->>Adapter: KubernetesResourceYAMLAdapter
    Adapter->>K8s: GET /apis/apps/v1/namespaces/production/deployments/order-api
    K8s-->>Adapter: Deployment found

    Service->>Port: fetch_resource(req)
    Port->>Adapter: KubernetesResourceYAMLAdapter
    Adapter->>K8s: GET deployment YAML
    K8s-->>Adapter: {kind: Deployment, spec: {replicas: 3, template: {containers: [{image: "registry/order-api:v2.3.1", resources: {limits: {cpu: "500m", memory: "512Mi"}}}]}}}

    Note over Service: Extract image tags, resource limits/requests

    Service-->>Tool: ResourceYAMLResponse(resource_found=True, image_tags=["v2.3.1"])
    Tool-->>MCP: {resource_found: true, image_tags: [...], resource_limits: {cpu: "500m", memory: "512Mi"}}
    MCP-->>AI: "order-api Deployment found. Image: registry/order-api:v2.3.1, Limits: cpu=500m, memory=512Mi. Full YAML returned."
```

### Flow 2 — Resource Not Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as resource_yaml
    participant Service as ResourceYAMLService

    AI->>Tool: resource_yaml("ghost", "production", "Deployment")
    Tool->>Service: get_resource()
    Note over Service: resource_exists → False<br/>404 from k8s API

    Service-->>Tool: resource_found=False, yaml_data={}
    Tool-->>AI: "Resource 'ghost' (Deployment) not found in namespace 'production'."
```

### Flow 3 — Secret Redacted

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as resource_yaml
    participant Service as ResourceYAMLService
    participant Adapter as KubernetesResourceYAMLAdapter
    participant K8s as Kubernetes API

    AI->>Tool: resource_yaml("db-creds", "production", "Secret")
    Tool->>Service: get_resource()
    Service->>Adapter: fetch_resource()
    Adapter->>K8s: GET secret
    K8s-->>Adapter: {kind: Secret, data: {DB_PASSWORD: "base64...", API_KEY: "base64..."}}

    Note over Service: _redact_secret()<br/>data values → "***REDACTED***"

    Service-->>Tool: yaml_data: {data: {DB_PASSWORD: "***REDACTED***", API_KEY: "***REDACTED***"}}
    Tool-->>AI: "Secret db-creds found. 3 keys: DB_PASSWORD, API_KEY, JWT_SECRET. Values redacted for security."
```

### Flow 4 — Checker Node: Secret Leak Prevention

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate secret redaction
    alt LLM reveals actual secret value in response
        Checker-->>LLM: ❌ FAIL — Secret values must never appear in output
    alt LLM says "resource not found" for RBAC-denied resource
        Checker-->>LLM: ⚠️ FLAG — differentiate "not found" from "permission denied"
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Secret redaction** — all `data` values replaced with `***REDACTED***`, only keys shown
- **Image tag extraction** — `spec.template.spec.containers[].image` + `initContainers`
- **Resource limits** — first container's `resources.limits` + `resources.requests` extracted
- **All resource types** — Deployment, Service, ConfigMap, Secret, Ingress, StatefulSet, DaemonSet

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_deployment_with_limits` | `tests/unit/test_resource_yaml.py` | ✅ |
| `test_resource_not_found` | `tests/unit/test_resource_yaml.py` | ✅ |
| `test_secret_redacted` | `tests/unit/test_resource_yaml.py` | ✅ |
| `test_returns_yaml` | `tests/unit/test_resource_yaml_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/resource_yaml.py` — ResourceYAMLResult, secret redaction
- `src/hexawyn/application/ports/driven/resource_yaml_port.py` — ResourceYAMLPort ABC
- `src/hexawyn/adapters/secondary/gitops/kubernetes_resource_yaml_adapter.py` — adapter
- `src/hexawyn/mcp/tools/resource_yaml.py` — MCP tool
