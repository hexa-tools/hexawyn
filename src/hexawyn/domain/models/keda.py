from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class KedaScaledObjectPhase(Enum):
    READY = "ready"
    NOT_READY = "not_ready"
    FALLBACK = "fallback"
    SCALED_TO_ZERO = "scaled_to_zero"
    COOLDOWN = "cooldown"
    ERROR = "error"
    UNKNOWN = "unknown"


class TriggerType(Enum):
    KAFKA = "kafka"
    RABBITMQ = "rabbitmq"
    PROMETHEUS = "prometheus"
    CRON = "cron"
    CPU = "cpu"
    MEMORY = "memory"
    AWS_SQS = "aws-sqs"
    AZURE_QUEUE = "azure-queue"
    GCP_PUBSUB = "gcp-pubsub"
    POSTGRESQL = "postgresql"
    REDIS = "redis"
    CUSTOM = "custom"


class AuthType(Enum):
    SECRET = "secret"
    ENV = "env"
    POD_IDENTITY = "pod_identity"
    NONE = "none"


class HPAStatus(Enum):
    ACTIVE = "active"
    NOT_ACTIVE = "not_active"
    UNAVAILABLE = "unavailable"


class ScaledJobPhase(Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    FAILED = "failed"
    COMPLETED = "completed"


@dataclass(frozen=True)
class KedaTrigger:
    type: TriggerType
    name: str
    metadata: dict[str, str]
    authentication_ref: str | None
    authentication_status: bool
    error_message: str | None


@dataclass(frozen=True)
class KedaScaledObject:
    name: str
    namespace: str
    phase: KedaScaledObjectPhase
    min_replicas: int
    max_replicas: int
    current_replicas: int
    hpa_target_replicas: int
    hpa_name: str | None
    hpa_status: HPAStatus
    triggers: list[KedaTrigger]
    cooldown_period_seconds: int
    last_scale_time: str | None
    idle_replicas: int
    fallback_replicas: int | None
    workload_kind: str
    workload_name: str
    ready: bool
    message: str | None


@dataclass(frozen=True)
class KedaTriggerAuth:
    name: str
    namespace: str
    kind: str
    trigger_types: list[TriggerType]
    auth_type: AuthType
    secret_names: list[str]
    environment_names: list[str]
    pod_identity_provider: str | None
    ready: bool
    message: str | None


@dataclass(frozen=True)
class KedaScaledJob:
    name: str
    namespace: str
    phase: ScaledJobPhase
    triggers: list[KedaTrigger]
    successful_jobs: int
    failed_jobs: int
    last_execution_time: str | None
    job_target_ref: str
    cooldown_period_seconds: int
    max_replica_count: int
    message: str | None


@dataclass(frozen=True)
class KedaDetectionResult:
    installed: bool
    version: str | None
    namespace: str | None
    total_scaledobjects: int
    ready_scaledobjects: int
    error_scaledobjects: int
    scaled_to_zero_count: int
    total_scaledjobs: int
    managed_namespaces: list[str]
