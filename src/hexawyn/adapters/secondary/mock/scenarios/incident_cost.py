INCIDENT_COST_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 55, "status": "degraded"},
    "pods": [
        {"name": "payment-api-1", "status": "Running", "restarts": 2, "namespace": "payments"},
        {"name": "checkout-api-1", "status": "Running", "restarts": 0, "namespace": "checkout"},
        {"name": "api-gateway-1", "status": "Running", "restarts": 1, "namespace": "production"},
    ],
    "metrics": {"cpu_usage_pct": 48, "memory_usage_pct": 55, "node_count": 8, "pod_count": 35},
    "findings": [
        {"severity": "high", "message": "Yesterday's outage: 90min downtime on payment-service", "remediation": "Estimated revenue loss: €3,200 based on 213 transactions/min × €25 avg"},
        {"severity": "high", "message": "Downtime: 14:03–15:33 UTC. Peak traffic window affected.", "remediation": "Business impact: 12,400 users affected, 3 enterprise SLA violations"},
        {"severity": "medium", "message": "Total incident cost: €3,200 revenue + €1,800 engineering time = €5,000", "remediation": "Recommend: circuit breaker, retry with backoff, canary deploys"},
        {"severity": "low", "message": "Confidence: 85% — based on transaction rate × downtime × average order value", "remediation": "For higher accuracy, integrate billing API for real revenue data"},
    ],
    "chips": ["Revenue loss", "Downtime", "Business impact", "Confidence 85%"],
    "slack_message": "💰 Yesterday's outage cost: €5,000 (€3,200 revenue + €1,800 engineering). SLA violations: 3.",
}
