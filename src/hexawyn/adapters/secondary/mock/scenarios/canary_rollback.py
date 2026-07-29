CANARY_ROLLBACK_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 68, "status": "degraded"},
    "pods": [
        {
            "name": "order-service-canary",
            "status": "Running",
            "restarts": 2,
            "namespace": "production",
        },
        {
            "name": "order-service-stable",
            "status": "Running",
            "restarts": 0,
            "namespace": "production",
        },
        {"name": "api-gateway-1", "status": "Running", "restarts": 0, "namespace": "production"},
    ],
    "metrics": {"cpu_usage_pct": 55, "memory_usage_pct": 60, "node_count": 8, "pod_count": 32},
    "findings": [
        {
            "severity": "critical",
            "message": "Canary v2.4 error rate: 12.4% vs stable v2.3: 0.3% — 41x increase",
            "remediation": "ROLLBACK immediately — canary is unsafe to promote",
        },
        {
            "severity": "high",
            "message": "Canary p99 latency: 1.2s vs stable: 180ms — 6.7x slower",
            "remediation": "Investigate code changes in v2.4 for N+1 query or blocking I/O",
        },
        {
            "severity": "high",
            "message": "Recommendation: ROLLBACK. Do not promote v2.4 to full production.",
            "remediation": "Fix the regression in dev, re-test, then re-deploy canary",
        },
    ],
    "chips": ["Canary vs Stable", "Error rate 12% vs 0.3%", "ROLLBACK", "Root cause"],
    "slack_message": "🚨 Canary v2.4: 12.4% error rate, 1.2s latency. RECOMMENDATION: ROLLBACK.",
}
