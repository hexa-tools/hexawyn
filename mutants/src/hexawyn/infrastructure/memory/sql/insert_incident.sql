INSERT INTO incidents (
    cluster_name,
    namespace,
    resource_name,
    resource_kind,
    tool_name,
    cause,
    symptoms,
    solution,
    severity,
    embedding,
    sanitized
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
