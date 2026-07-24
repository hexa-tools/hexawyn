PLATFORM_HEALTH_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 72, "status": "degraded"},
    "pods": [
        {"name": "api-gateway-1", "status": "Running", "restarts": 2, "namespace": "production"},
        {"name": "payment-api-1", "status": "Running", "restarts": 0, "namespace": "payments"},
        {"name": "checkout-api-1", "status": "Running", "restarts": 1, "namespace": "checkout"},
        {"name": "auth-service-1", "status": "Running", "restarts": 0, "namespace": "auth"},
        {"name": "inventory-api-1", "status": "Running", "restarts": 0, "namespace": "inventory"},
        {"name": "scheduler-1", "status": "Running", "restarts": 0, "namespace": "jobs"},
    ],
    "metrics": {"cpu_usage_pct": 64, "memory_usage_pct": 71, "node_count": 10, "pod_count": 42},
    "findings": [
        {"severity": "medium", "message": "Health score: 72/100 — degraded but operational", "remediation": "Monitor SLOs and address high-priority findings"},
        {"severity": "high", "message": "Predicted: payment-api may breach SLO in 3 days at current error rate", "remediation": "Investigate error budget burn rate"},
        {"severity": "medium", "message": "Monthly cloud spend: €12,430 — on track for €15,200 (budget €15,000)", "remediation": "Review dev and staging right-sizing"},
        {"severity": "low", "message": "3 incidents this week, avg MTTR 45min — improving vs last week (7 incidents, 90min)", "remediation": "On-call process improvements showing results"},
    ],
    "chips": ["Health score", "Cost forecast", "SLO prediction", "Incident trend", "Budget status"],
    "slack_message": "📊 Platform weekly: Health 72, €12.4k spend, 3 incidents, SLO at risk. Budget: 98% consumed.",
}
