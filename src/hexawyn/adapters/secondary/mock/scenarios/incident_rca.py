INCIDENT_RCA_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 30, "status": "critical"},
    "pods": [
        {"name": "payment-api-1", "status": "CrashLoopBackOff", "restarts": 67, "namespace": "payments"},
        {"name": "payment-worker-1", "status": "CrashLoopBackOff", "restarts": 45, "namespace": "payments"},
        {"name": "payment-db-proxy-1", "status": "Running", "restarts": 3, "namespace": "payments"},
        {"name": "api-gateway-1", "status": "Running", "restarts": 12, "namespace": "production"},
    ],
    "metrics": {"cpu_usage_pct": 92, "memory_usage_pct": 97, "node_count": 10, "pod_count": 40},
    "findings": [
        {"severity": "critical", "message": "Payment outage: 90min downtime, 12,400 affected users, €3,200 revenue loss", "remediation": "Root cause: database migration changed column type without updating application code"},
        {"severity": "critical", "message": "payment-api and payment-worker both CrashLoopBackOff — cascading failure", "remediation": "Fix: rollback DB migration, restart payment services, validate"},
        {"severity": "high", "message": "api-gateway 12 restarts due to timeout floods from failing payment backends", "remediation": "Add circuit breaker to prevent cascading failures"},
        {"severity": "medium", "message": "Incident timeline: 14:03 DB migration → 14:05 first CrashLoop → 14:08 cascading → 15:30 resolution", "remediation": "Prevent: require dual-write during migrations, canary deploy first"},
    ],
    "chips": ["RCA report", "Timeline", "Revenue impact", "Prevention plan"],
    "slack_message": "🚨 PAYMENT OUTAGE: 90min, €3,200 loss. Root cause: DB migration. Post-mortem ready.",
}
