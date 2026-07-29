from dataclasses import dataclass, field
from typing import TypedDict


class MetricResultDict(TypedDict):
    labels: dict[str, str]
    value: float
    values: list[list[float]]
    formatted_value: str


@dataclass
class ExecutePrometheusQueryResponse:
    query: str = ""
    query_type: str = ""
    status: str = ""
    result_type: str = ""
    results: list[MetricResultDict] = field(default_factory=list)
    result_count: int = 0
    truncated: bool = False
    no_data: bool = False
    summary: str = ""
