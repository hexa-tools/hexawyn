INSERT INTO consolidated_knowledge (
    id, pattern, resource_name, resource_kind, namespace, tool_name,
    cluster_name, occurrence_count, first_seen, last_seen,
    source_incident_ids, embedding, weight, confidence
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
