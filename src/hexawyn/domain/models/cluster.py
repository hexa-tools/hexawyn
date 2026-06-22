from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum


class ClusterHealth(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class CloudProvider(Enum):
    VANILLA = "vanilla"
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    OPENSHIFT = "openshift"
    DATADOG = "datadog"
    DEMO = "demo"


@dataclass
class ClusterContext:
    name: str
    namespace: str = "default"
    provider: CloudProvider = CloudProvider.VANILLA
    api_server: str = ""


@dataclass
class ClusterScore:
    overall: int  # 0-100
    health: ClusterHealth
    cluster_name: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    breakdown: dict[str, int] = field(default_factory=dict)
    issues: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
