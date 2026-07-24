PRODUCTION_OUTAGE_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 42, "status": "critical"},
    "pods": [
        {"name": "payment-api-7f9b", "status": "CrashLoopBackOff", "restarts": 89, "namespace": "payments"},
        {"name": "checkout-api-3c2a", "status": "CrashLoopBackOff", "restarts": 45, "namespace": "checkout"},
        {"name": "inventory-worker-1a4d", "status": "CrashLoopBackOff", "restarts": 32, "namespace": "inventory"},
        {"name": "data-processor-5e6f", "status": "OOMKilled", "restarts": 12, "namespace": "data-pipeline"},
        {"name": "auth-service-8g1h", "status": "Running", "restarts": 0, "namespace": "auth"},
    ],
    "metrics": {"cpu_usage_pct": 88, "memory_usage_pct": 94, "node_count": 12, "pod_count": 48},
    "findings": [
        {"severity": "critical", "message": "payment-api CrashLoopBackOff (89 restarts) — probable OOM or startup failure", "remediation": "Check pod logs for exit code, verify resource limits"},
        {"severity": "critical", "message": "OOMKill in data-processor — memory limit too low", "remediation": "Increase memory limit from 256Mi to 1Gi"},
        {"severity": "high", "message": "checkout-api and inventory-worker both crashing — possible shared dependency failure", "remediation": "Check upstream database or API gateway health"},
    ],
    "chips": ["CrashLoop payment-api", "OOM data-processor", "Root cause?", "Recovery plan"],
    "slack_message": "🚨 CRITICAL: prod-eu — 3 CrashLoopBackOff + 1 OOMKill. Health score 42/100. On-call paged.",
}
