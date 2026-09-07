INSERT INTO tekton_pipeline_runs (
    name,
    namespace,
    pipeline_name,
    status,
    duration_seconds,
    start_time,
    completion_time
)
VALUES (?, ?, ?, ?, ?, ?, ?)
ON CONFLICT (name) DO UPDATE SET
    namespace = excluded.namespace,
    pipeline_name = excluded.pipeline_name,
    status = excluded.status,
    duration_seconds = excluded.duration_seconds,
    start_time = excluded.start_time,
    completion_time = excluded.completion_time;
