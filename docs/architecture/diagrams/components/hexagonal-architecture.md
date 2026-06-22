# Hexagonal Architecture — Ports & Adapters

High-level view of hexawyn's hexagonal architecture showing how domain logic, application ports, and adapters interact.

```mermaid
graph TB
    subgraph "Primary Adapters (Driving)"
        CLI[CLI Textual TUI]
        MCP[MCP Server FastMCP]
        Slack[Slack Chat Adapter]
    end

    subgraph "Application"
        subgraph "Ports — Driving"
            PI[parse_intent use case]
            HC[health_check use case]
        end
        subgraph "Services"
            QM[QuotaManager]
            AF[AdapterFactory]
        end
        subgraph "Ports — Driven"
            K8s[K8sPort]
            Metrics[MetricsPort]
            Traces[TracesPort]
            Logs[LogsPort]
            Memory[MemoryPort]
        end
    end

    subgraph "Domain"
        Models[ClusterContext<br/>InvestigationResult<br/>UsageQuota]
        Errors[HexawynError<br/>QuotaExceededError]
        Services[Domain Services]
    end

    subgraph "Secondary Adapters (Driven)"
        Demo[DemoAdapter mock/]
        Vanilla[VanillaAdapter]
        AWS[AWS Adapter EKS]
        Azure[Azure Adapter AKS]
        GCP[GCP Adapter GKE]
        OpenShift[OpenShift Adapter]
        Datadog[Datadog Adapter]
        DuckDB[DuckDB memory/]
    end

    subgraph "External"
        K8sAPI[Kubernetes API]
        CloudWatch[CloudWatch]
        Prometheus[Prometheus]
    end

    CLI --> PI
    MCP --> PI
    Slack --> PI

    PI --> QM
    PI --> AF

    AF --> Demo
    AF --> Vanilla
    AF --> AWS
    AF --> Azure
    AF --> GCP
    AF --> OpenShift
    AF --> Datadog

    Demo --> K8s
    Vanilla --> K8s
    AWS --> K8s
    AWS --> CloudWatch
    GCP --> Prometheus

    K8s --> K8sAPI

    QM --> DuckDB

    Domain --> Models
    Domain --> Errors
```

## Key Points

- Domain has ZERO external dependencies — pure Python only (enforced by hexa_guard R1)
- Adapters NEVER import domain directly — always go through application/ports/ (enforced by hexa_guard R5)
- AdapterFactory selects the right secondary adapter based on cluster name and installed packages
- DemoAdapter lives in mock/ only — never referenced in production code paths (enforced by hexa_guard R10)
- All SQL lives in .sql files under infrastructure/memory/sql/ — never inline in Python
