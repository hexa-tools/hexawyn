LATENCY_SPIKE_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 70, "status": "degraded"},
    "pods": [
        {"name": "payment-api-v2.4", "status": "Running", "restarts": 3, "namespace": "payments"},
        {"name": "payment-api-v2.3", "status": "Running", "restarts": 0, "namespace": "payments"},
        {"name": "db-proxy-1", "status": "Running", "restarts": 0, "namespace": "payments"},
        {"name": "redis-cache-1", "status": "Running", "restarts": 0, "namespace": "payments"},
        {"name": "api-gateway-1", "status": "Running", "restarts": 0, "namespace": "production"},
    ],
    "metrics": {"cpu_usage_pct": 72, "memory_usage_pct": 68, "node_count": 10, "pod_count": 38},
    "findings": [
        {"severity": "high", "message": "payment-api p99 latency: 800ms (baseline 200ms) — 4x increase after v2.4 deploy", "remediation": "Compare spans between v2.3 and v2.4, check DB query performance"},
        {"severity": "high", "message": "Slowest span: db-proxy → PostgreSQL query taking 650ms (was 80ms)", "remediation": "Check for missing index, query plan change, or connection pool exhaustion"},
        {"severity": "medium", "message": "Error rate unchanged (0.2%) — latency only, no errors", "remediation": "This is a performance regression, not a functionality bug"},
    ],
    "chips": ["p99 latency 800ms", "DB query bottleneck", "v2.4 regression", "Rollback?"],
    "slack_message": "⚠️ payment-api p99: 800ms (+4x). DB query bottleneck detected.",
}
