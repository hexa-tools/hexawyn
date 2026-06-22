DATADOG_SCENARIO = {
    "context": {"name": "prod-eks-datadog", "cluster": "eks-prod", "provider": "aws"},
    "health": {"score": 79, "status": "degraded"},
    "pods": [
        {"name": "payments-api-7d9f8b-m3ql", "status": "Running", "restarts": 6, "namespace": "payments"},
        {"name": "frontend-4c2d9f-xp5j", "status": "Running", "restarts": 1, "namespace": "web"},
    ],
    "metrics": {"cpu_usage_pct": 72.1, "memory_usage_pct": 88.4, "node_count": 10, "pod_count": 42},
    "findings": [
        {
            "severity": "critical",
            "message": "Datadog monitor Alert: payments-api latency spike to 820ms p99",
            "remediation": "Check DB connection pool exhaustion and slow queries",
        },
        {
            "severity": "high",
            "message": "Datadog monitor Warn: frontend error rate 5.2% exceeds 2% threshold",
            "remediation": "Investigate increased 500 errors in frontend logs",
        },
    ],
    "chips": ["payments-api p99 820ms", "frontend error rate 5.2%", "Memory 88%"],
    "slack_message": "Alert: Datadog — payments-api p99=820ms, frontend error rate 5.2%. Score 79.",
    "triggered_monitors": [
        {"name": "payments-api latency spike", "status": "Alert", "value": 820},
        {"name": "frontend error rate", "status": "Warn", "value": 5.2},
    ],
    "apm_services": [
        {"service": "payments-api", "p99_ms": 820, "error_rate": 1.3},
        {"service": "frontend", "p99_ms": 245, "error_rate": 5.2},
    ],
}
