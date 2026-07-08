from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import TypedDict


class TaskRunNodeDict(TypedDict):
    name: str
    start_time: str | None
    duration_seconds: float
    status: str
    dependencies: list[str]
    is_on_critical_path: bool
    failure_reason: str


@dataclass
class TaskRunNode:
    name: str
    start_time: datetime | None = None
    duration_seconds: float = 0.0
    status: str = ""
    dependencies: list[str] = field(default_factory=list)
    is_on_critical_path: bool = False
    failure_reason: str = ""


@dataclass
class DAGEdge:
    source: str
    target: str


@dataclass
class PipelineDAG:
    pipeline_run_name: str
    namespace: str
    pipeline_status: str = ""
    pipeline_ref: str = ""
    task_runs: list[TaskRunNode] = field(default_factory=list)
    critical_path: list[str] = field(default_factory=list)
    failed_tasks: list[str] = field(default_factory=list)
    skipped_tasks: list[str] = field(default_factory=list)
    cancelled_at_tasks: list[str] = field(default_factory=list)
