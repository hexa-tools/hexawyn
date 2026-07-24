CLUSTER_AUDIT_SCENARIO = {
    "context": {"name": "prod-eu", "cluster": "prod-eu", "provider": "vanilla"},
    "health": {"score": 61, "status": "degraded"},
    "pods": [
        {"name": "security-scanner-1", "status": "Running", "restarts": 0, "namespace": "security"},
        {"name": "db-admin-1", "status": "Running", "restarts": 0, "namespace": "databases"},
        {"name": "legacy-app-1", "status": "Running", "restarts": 3, "namespace": "legacy"},
        {"name": "api-gateway-1", "status": "Running", "restarts": 0, "namespace": "production"},
        {"name": "monitoring-1", "status": "Running", "restarts": 0, "namespace": "monitoring"},
    ],
    "metrics": {"cpu_usage_pct": 56, "memory_usage_pct": 62, "node_count": 8, "pod_count": 35},
    "findings": [
        {"severity": "critical", "message": "2 pods running as root with privileged: true in production", "remediation": "Apply restricted Pod Security Standard"},
        {"severity": "critical", "message": "3 service accounts with cluster-admin — blast radius too large", "remediation": "Audit RBAC, apply least privilege"},
        {"severity": "high", "message": "7 TLS certificates expire in < 30 days, 2 already expired", "remediation": "Review cert-manager configuration"},
        {"severity": "high", "message": "5 secrets not rotated in > 90 days — compliance violation", "remediation": "Rotate db-passwords, api-keys, tls-keys"},
        {"severity": "medium", "message": "Compliance score: 61/100 — TLS, RBAC, and secrets need attention", "remediation": "Prioritize: 1) Prune cluster-admin 2) Fix expired certs 3) Rotate secrets"},
    ],
    "chips": ["Privileged pods", "cluster-admin audit", "TLS expiry", "Secret rotation", "Compliance score"],
    "slack_message": "🔒 Security audit: 2 privileged pods, 3 cluster-admin, 7 TLS expiring. Score: 61/100.",
}
