INSERT INTO tekton_task_runs (
    name,
    namespace,
    task_name,
    pipeline_run_name,
    duration_seconds
)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT (name) DO UPDATE SET
    namespace = excluded.namespace,
    task_name = excluded.task_name,
    pipeline_run_name = excluded.pipeline_run_name,
    duration_seconds = excluded.duration_seconds;
