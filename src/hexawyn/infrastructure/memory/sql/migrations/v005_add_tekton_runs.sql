-- v005: Tekton PipelineRun/TaskRun history — feeds pipeline performance baseline
CREATE TABLE IF NOT EXISTS tekton_pipeline_runs (
    name VARCHAR PRIMARY KEY,
    namespace VARCHAR NOT NULL,
    pipeline_name VARCHAR NOT NULL,
    status VARCHAR,
    duration_seconds INTEGER,
    start_time VARCHAR,
    completion_time VARCHAR,
    ingested_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_tekton_pipeline_runs_pipeline
    ON tekton_pipeline_runs(pipeline_name, start_time);

CREATE TABLE IF NOT EXISTS tekton_task_runs (
    name VARCHAR PRIMARY KEY,
    namespace VARCHAR NOT NULL,
    task_name VARCHAR,
    pipeline_run_name VARCHAR NOT NULL,
    duration_seconds INTEGER,
    ingested_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_tekton_task_runs_pipeline_run
    ON tekton_task_runs(pipeline_run_name);
