NAMESPACE_DEGRADED_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 45, "status": "critical"},
    "pods": [
        {
            "name": "checkout-api-7f9b",
            "status": "CrashLoopBackOff",
            "restarts": 56,
            "namespace": "checkout",
        },
        {
            "name": "checkout-worker-3c2a",
            "status": "Running",
            "restarts": 8,
            "namespace": "checkout",
        },
        {
            "name": "checkout-redis-1a4d",
            "status": "Running",
            "restarts": 0,
            "namespace": "checkout",
        },
        {
            "name": "checkout-frontend-9g1h",
            "status": "Pending",
            "restarts": 0,
            "namespace": "checkout",
        },
        {
            "name": "checkout-scheduler-4b2c",
            "status": "Running",
            "restarts": 0,
            "namespace": "checkout",
        },
    ],
    "metrics": {"cpu_usage_pct": 85, "memory_usage_pct": 91, "node_count": 10, "pod_count": 42},
    "findings": [
        {
            "severity": "critical",
            "message": "checkout-api CrashLoopBackOff for 56 restarts — OOMKill detected in previous pod",  # noqa: E501
            "remediation": "Increase memory limit, investigate memory leak",
        },
        {
            "severity": "high",
            "message": "checkout-frontend stuck Pending — no nodes with required GPU available",
            "remediation": "Check node affinity and GPU scheduling",
        },
        {
            "severity": "medium",
            "message": "checkout-worker 8 restarts with intermittent connection failures",
            "remediation": "Check network policies and upstream dependencies",
        },
        {
            "severity": "low",
            "message": "Events: OOMKilled, BackOff, FailedScheduling detected in last 30min",
            "remediation": "Correlate events with pod lifecycle for timeline",
        },
    ],
    "chips": ["CrashLoop + OOM", "Event timeline", "Root cause", "Fix plan"],
    "slack_message": "🚨 checkout namespace critical — CrashLoop, OOM, Pending. Health 45/100.",
}
