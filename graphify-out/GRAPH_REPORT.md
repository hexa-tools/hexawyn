# Graph Report - src  (2026-07-27)

## Corpus Check
- Large corpus: 1693 files · ~169,279 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 8634 nodes · 21141 edges · 524 communities (511 shown, 13 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 2144 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Gcp / Aws
- Vanilla
- Ports / Vanilla
- Secret / Services
- Ports / Use
- Label / Use
- Mock / Ports
- Platform / Services
- Ports / Use
- Namespace / Services
- External / Use
- Quota / Config
- Log / Use
- Sla / Ports
- Config / Http
- Log / Services
- Budget / Services
- Consolidation / Ports
- Presentation / Asides
- Gitops / Azure
- Openshift / Cluster
- Gcp / Aws
- Datadog / Gcp
- Openshift / Machine
- Ports / Pipeline
- Openshift / Ports
- Use / Case
- Use / Case
- Ports / Historical
- Gitops / Ports
- Config / Machine
- Manual / Services
- Cross / Ports
- Use / Case
- Use / Case
- Screens / Session
- Gitops / Azure
- Ports / Cluster
- Monthly / Use
- Memory / Duckdb
- Hot / Services
- Namespace / Services
- Use / Case
- Use / Case
- Kubernetes / Ports
- Adaptive / Use
- Pod / Use
- Ports / Gitops
- Ports / Services
- Pipeline / Ports
- Image / Services
- Rbac / Services
- Use / Case
- Cost / Services
- License / Errors
- Services / Log
- Aws / Ports
- Gitops / Ports
- Quota / Ports
- Rightsizing / Services
- Gitops / Ports
- Ports / Outdated
- Gitops / Ports
- Ports / Kustomize
- Services / Event
- Metrics / Use
- Certificate / Ports
- Gitops / Certificates
- Datadog / Kubernetes
- Gitops / Ports
- Gitops / Ports
- Gitops / Ports
- Use / Case
- Use / Case
- Schedule / Commands
- Canary / Ports
- Ports / Use
- Resource / Ports
- Memory / Use
- Simulation / Services
- Gitops / Ports
- Version / Ports
- Ports / Gitops
- Ports / Tls
- Ports / Use
- Log / Use
- Event / Services
- Deployment / Ports
- Admin / Ports
- Ports / Use
- Gitops / Errors
- Tls / Ports
- Trace / Ports
- Metric / Ports
- Security / Ports
- Use / Case
- Use / Case
- Config / Kubernetes
- Aws
- Redundant / Ports
- Tools / Custom
- Error / Services
- Ports / Rollouts
- Pipeline / Ports
- Use / Case
- Sensitive / Ports
- Cost / Ports
- P99 / Ports
- Slowest / Ports
- Slo / Ports
- Use / Case
- Use / Case
- Etcd / Ports
- Gitops / Ports
- Ports / Use
- Use / Case
- Zombie / Services
- Helm / Services
- Gitops / Keda
- Pipeline / Ports
- Error / Ports
- Use / Case
- Use / Case
- Server / Config
- Headroom / Services
- Stack / Presentation
- Ports / Gitops
- Use / Case
- Schedule / Services
- Services / Event
- Pod / Services
- Ports / Use
- Anonymization / Logging
- Usage / Monitoring
- Ports / Gitops
- Gitops / Ports
- Cluster / Use
- Ports / Openshift
- Schedule / Services
- Topology / Services
- Spike / Services
- Datadog
- Istio / Ports
- Gitops / Ports
- Slack / Commands
- Ports / Tools
- Use / Case
- Use / Case
- Use / Case
- Incident / Services
- Configuration / Services
- Azure
- Datadog / Ports
- Optimization / Services
- License / Screens
- Cache / Memory
- Ports / Gitops
- Ports / Container
- Use / Case
- Security / Services
- Aws
- Fleet / Config
- Gitops / Ports
- Slack / Ports
- Ports / Memory
- Use / Case
- Use / Case
- Errors / Historicaldatawindowexpirederror
- Services / Failure
- Gitops / Ports
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Gcp / Ports
- Ports / Use
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Services / Anomaly
- Use / Case
- Slack / Ports
- Azure
- Memory / Duckdb
- Ports / Use
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Services / Topology
- Fleet / Services
- Ports / Use
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Gitops / Ports
- Ports / Pricing
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Commands / Auth
- Gitops / Ports
- Gitops
- Kubernetes / Ports
- Ports
- Screens / Welcome
- Tools / Cluster
- Network / Services
- Probe / Services
- Gcp
- Gitops / Ports
- Ports / Gitops
- Commands / Cache
- Cost / Services
- Gitops
- Ports / Logger
- Tools / Hot
- Screens / Context
- Services / Event
- Services / Log
- Mttr / Services
- Screens / Provider
- Services / Cluster
- Gitops
- Ports / Services
- Cost
- Slack
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Tools / Prometheus
- Commands / Cluster
- Use / Case
- Use / Case
- Use / Case
- Log / Services
- Topology
- Config / Telemetry
- License / Activation
- Slack / Config
- Gitops
- Services / Anomaly
- Tools / Generate
- Ports
- Security
- Tools / Snapshots
- Config / Region
- Services / Cluster
- Services / Retrieval
- Config / Schedule
- Constants / Services
- Semantic
- Services / Network
- Memory / Duckdb
- Ports
- Commands / Slack
- Config / First
- Logging / Tool
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case
- Use / Case

## God Nodes (most connected - your core abstractions)
1. `VanillaAdapter` - 193 edges
2. `ClusterUnreachableError` - 170 edges
3. `InsufficientPermissionsError` - 149 edges
4. `K8sPort` - 136 edges
5. `PodInfo` - 68 edges
6. `ResourceNotFoundError` - 58 edges
7. `KedaPort` - 47 edges
8. `ClusterContext` - 46 edges
9. `HexawynError` - 45 edges
10. `CertManagerPort` - 44 edges

## Surprising Connections (you probably didn't know these)
- `PodAnomalyDetectionRequest` --uses--> `EventSeverity`  [INFERRED]
  hexawyn/domain/models/pod_anomaly.py → hexawyn/domain/models/event.py
- `SlackChatAdapter` --uses--> `ChatPort`  [INFERRED]
  hexawyn/adapters/primary/slack/slack_chat_adapter.py → hexawyn/application/ports/primary/chat_port.py
- `SlackEventServer` --uses--> `ChatPort`  [INFERRED]
  hexawyn/adapters/primary/slack/slack_event_server.py → hexawyn/application/ports/primary/chat_port.py
- `SlackSocketClient` --uses--> `SlackHttpClient`  [INFERRED]
  hexawyn/adapters/primary/slack/slack_socket_client.py → hexawyn/adapters/secondary/slack/slack_http_client.py
- `SlackSocketClient` --uses--> `MessagePublisherPort`  [INFERRED]
  hexawyn/adapters/primary/slack/slack_socket_client.py → hexawyn/application/ports/driven/message_publisher_port.py

## Import Cycles
- None detected.

## Communities (524 total, 13 thin omitted)

### Community 0 - "Gcp / Aws"
Cohesion: 0.04
Nodes (71): EntryPoint, CloudProvider, ABC, ClusterContext, Does this provider support the given cluster?, Build the adapter bundle for this cluster., Display name: 'AWS EKS', 'Azure AKS', etc., CLI badge: '☁ AWS', '☁ Azure', etc. (+63 more)

### Community 1 - "Vanilla"
Cohesion: 0.04
Nodes (18): _deployment_key_from_pod(), ClusterContext, PipelineRunInfo, Returns {namespace/workload-prefix: {cpu_cores, memory_mi}}., Estimate daily cluster cost from K8s resource requests.          Returns `days`, List namespace-scoped custom objects., Returns {namespace/deployment_name: min_replicas}., Returns {namespace/pod_name: value} from a Prometheus instant query. (+10 more)

### Community 2 - "Ports / Vanilla"
Cohesion: 0.04
Nodes (76): _build_daily_cost_entries(), _compute_namespace_daily_costs(), _compute_pod_resources(), _container_request(), _extract_container_data(), _get_workload_type(), KubernetesAppsApi, KubernetesCoreApi (+68 more)

### Community 3 - "Secret / Services"
Cohesion: 0.05
Nodes (67): _extract_secret_names(), KubernetesSecretAuditAdapter, Any, Exception, ManagedFieldsEntryRaw, Secondary adapter — enumerates every Secret (with managedFields) via     the K8s, _references_from_deployment(), _references_from_pod() (+59 more)

### Community 4 - "Ports / Use"
Cohesion: 0.06
Nodes (64): KubernetesImageInventoryAdapter, Any, Exception, Secondary adapter — enumerates every unique container image currently     runnin, _to_running_images(), _translate_error(), _detect_base_image(), _parse_trivy_payload() (+56 more)

### Community 5 - "Label / Use"
Cohesion: 0.06
Nodes (50): KubernetesLabelSearchAdapter, _pod_ready(), V1Deployment, V1Pod, Secondary adapter — searches pods/deployments/services/configmaps by     label s, _to_non_pod_raw(), _to_pod_raw(), MatchedResourceRaw (+42 more)

### Community 6 - "Mock / Ports"
Cohesion: 0.03
Nodes (29): DemoAdapter, ClusterContext, SlowTrace, In-memory demo adapter for testing without a real cluster., ExtendedClusterPort, PipelineRunInfo, ABC, Port for extended cluster features — projects, routes, pipelines (OpenShift, Tek (+21 more)

### Community 7 - "Platform / Services"
Cohesion: 0.06
Nodes (49): PlatformReliabilityAdapter, Protocol, Assembles reliability inputs from the incident/MTTR sources and pricing     conf, Facade over the incident / MTTR / pricing sources for the CTO report.      Deleg, ReliabilityDataSource, EmptyReliabilityDataSource, Default reliability source used until the incident/MTTR roll-up is wired     in., PlatformReliabilityPort (+41 more)

### Community 8 - "Ports / Use"
Cohesion: 0.07
Nodes (38): OTelSpanBreakdownAdapter, SpanBreakdown, OTelTraceLogAdapter, ABC, SpanBreakdown, SpanBottleneckPort, ABC, TraceLogCorrelationPort (+30 more)

### Community 9 - "Namespace / Services"
Cohesion: 0.07
Nodes (51): DeploymentClassification, DeploymentStatusRaw, NamespaceOverviewPort, NamespaceOverviewRawData, PodStatusRaw, ABC, TypedDict, Driven port: fetches pods, deployments, service count, and HPAs for     one name (+43 more)

### Community 10 - "External / Use"
Cohesion: 0.06
Nodes (44): KubernetesExternalExposureAdapter, Any, Exception, Secondary adapter — enumerates every Service across all namespaces via     the K, _to_service_raw(), _translate_error(), ExternalExposureAuditPort, ABC (+36 more)

### Community 11 - "Quota / Config"
Cohesion: 0.07
Nodes (46): _resolve_tier(), ABC, QuotaStorePort, Get investigation quota for a given month., Get Slack alert quota for a given month., Increment investigation counter for a given month., Increment Slack alert counter for a given month., Port for quota storage — abstracts DuckDB away from quota_manager. (+38 more)

### Community 12 - "Log / Use"
Cohesion: 0.08
Nodes (53): TypedDict, RawPodLogData, ABC, SemanticLogSearchServicePort, SemanticLogSearchCommand, MatchedLogLineDict, PodLogMatchDict, TypedDict (+45 more)

### Community 13 - "Sla / Ports"
Cohesion: 0.06
Nodes (42): Protocol, QuarterSlaSource, Facade over the reliability/SLO sources for quarterly SLA reporting.      Delega, Assembles quarter-level SLA data from the weekly reliability / SLO     sources i, SlaReportAdapter, EmptyQuarterSlaSource, Default quarterly SLA source used until a persistent reliability roll-up     is, ABC (+34 more)

### Community 14 - "Config / Http"
Cohesion: 0.06
Nodes (36): ABC, Any, TypedDict, QuotaCheckResult, RuntimePort, StartupScanResult, _extract_float_list(), _extract_string_list() (+28 more)

### Community 15 - "Log / Services"
Cohesion: 0.08
Nodes (32): LogAnalysisConstants, Thresholds and limits for log analysis strategies., DeduplicatedLine, LogAnalysisContext, LogAnalysisResult, RankedEvent, Output of a log analysis strategy., A log line collapsed from repeated occurrences, with its total count. (+24 more)

### Community 16 - "Budget / Services"
Cohesion: 0.07
Nodes (44): BudgetProjectionAdapter, _month_of(), Aggregates the daily cost source into monthly history by category.      Daily co, _to_monthly_raw(), BudgetProjectionPort, MonthlyCostRaw, ABC, TypedDict (+36 more)

### Community 17 - "Consolidation / Ports"
Cohesion: 0.06
Nodes (33): ConsolidationConfig, DomainConfig, ConsolidationConfig, ConsolidationPort, ABC, TypedDict, Consolidation port — memory consolidation driven port., Group incidents by namespace+resource+tool, return tuples. (+25 more)

### Community 18 - "Presentation / Asides"
Cohesion: 0.09
Nodes (44): build_aside_lines(), Any, crashloop_finding_count(), failed_pod_count(), finding_message(), issue_name(), issue_reason(), kubectl_current_context() (+36 more)

### Community 19 - "Gitops / Azure"
Cohesion: 0.07
Nodes (41): AzureLogAnalyticsAdapter, LogsClient, _LogsResult, _LogsTable, Protocol, Minimal contract for the azure-monitor-query LogsQueryClient used here., LogSearchPort backed by Azure Log Analytics (ContainerLogV2) via KQL.      Reads, KubernetesImageDriftAdapter (+33 more)

### Community 20 - "Openshift / Cluster"
Cohesion: 0.08
Nodes (36): _condition_status(), _conditions(), CustomObjectsApi, _degraded_since(), _find_condition(), _items(), OpenShiftClusterOperatorAdapter, Protocol (+28 more)

### Community 21 - "Gcp / Aws"
Cohesion: 0.07
Nodes (37): AWSCostAdapter, CostExplorerClient, _parse_namespace_costs(), Exception, Protocol, Minimal contract for the boto3 Cost Explorer client used here., CostEstimationPort backed by AWS Cost Explorer.      Queries the Cost Explorer A, _translate_error() (+29 more)

### Community 22 - "Datadog / Gcp"
Cohesion: 0.08
Nodes (32): _LogEvent, _build_logs_api(), DatadogLogsAdapter, _Log, _LogAttribute, LogsApi, _LogsResponse, Exception (+24 more)

### Community 23 - "Openshift / Machine"
Cohesion: 0.08
Nodes (36): _as_int(), _conditions(), CustomObjectsApi, _find_condition(), _is_true(), _items(), _mapping(), OpenShiftMachineConfigAdapter (+28 more)

### Community 24 - "Ports / Pipeline"
Cohesion: 0.07
Nodes (39): _extract_failure_reason(), _extract_pipeline_ref(), _extract_run_after(), _extract_status(), PipelineRunRecord, TaskRunRecord, TektonPipelineTracerAdapter — fetches PipelineRun + child TaskRuns from K8s CRDs, TektonPipelineTracerAdapter (+31 more)

### Community 25 - "Openshift / Ports"
Cohesion: 0.06
Nodes (29): _items(), _mapping(), _metadata(), OpenShiftAdapter, ClusterContext, Exception, OpenShift adapter — understands Projects, Routes, SCCs and ImageStreams.      St, _to_image_stream() (+21 more)

### Community 26 - "Use / Case"
Cohesion: 0.08
Nodes (35): _compute_duration_seconds(), _extract_pipeline_ref(), _extract_status(), KubernetesTektonAdapter, PipelineRunRecord, Secondary adapter — reads Tekton PipelineRun CRDs from the K8s API., Return (status_str, failure_reason)., _to_record() (+27 more)

### Community 27 - "Use / Case"
Cohesion: 0.08
Nodes (31): IncidentMemoryPort, ABC, Persist a completed investigation for later similarity retrieval.          Best-, LogEntry, LogsPort, ABC, TypedDict, Port for log search — CloudWatch, Log Analytics, Cloud Logging, Datadog. (+23 more)

### Community 28 - "Ports / Historical"
Cohesion: 0.08
Nodes (30): KubeArchiveHTTPAdapter, HistoricalComparisonResult, HistoricalPodInfo, KubeArchivePort, KubeArchiveQuery, KubeArchiveResponse, ABC, TypedDict (+22 more)

### Community 29 - "Gitops / Ports"
Cohesion: 0.09
Nodes (34): IncidentCostAdapter, IncidentCostSource, Protocol, Assembles an incident's business facts and the configured financial     paramete, Facade over the incident source and the business financial config.      Delegate, _as_float(), _business_section(), ConfigIncidentCostSource (+26 more)

### Community 30 - "Config / Machine"
Cohesion: 0.06
Nodes (44): account(), _activate_license(), _format_expiry(), argument, command, option, Response, hexa auth — manage hexawyn cloud authentication and licensing. (+36 more)

### Community 31 - "Manual / Services"
Cohesion: 0.08
Nodes (37): ManualChangeOutsideGitOpsServicePort, ABC, ManualChangeOutsideGitOpsCommand, ManualChangeOutsideGitOpsResponse, ManualChangeOutsideGitopsCommand, _index_audit_events(), ManualChangeOutsideGitopsUseCase, GitopsDriftAuditPort (+29 more)

### Community 32 - "Cross / Ports"
Cohesion: 0.10
Nodes (31): CrossClusterIncidentAdapter, FailureSignatureSource, Protocol, EmptyFailureSignatureSource, ClusterFailureSignature, CrossClusterIncidentPort, ABC, TypedDict (+23 more)

### Community 33 - "Use / Case"
Cohesion: 0.10
Nodes (34): KubernetesLiveResourceAdapter, Secondary adapter — lists live Deployments and ConfigMaps, extracting     labels, _to_live_resource(), LiveResourcePort, LiveResourceRaw, ABC, TypedDict, Driven port: lists live Kubernetes resources (currently Deployment     and Confi (+26 more)

### Community 34 - "Use / Case"
Cohesion: 0.08
Nodes (29): ListOpenshiftImagestreamsCommand, ListOpenshiftImagestreamsUseCase, ListOpenshiftImagestreamsResponse, ListOpenshiftProjectsCommand, ListOpenshiftProjectsUseCase, ListOpenshiftProjectsResponse, ListOpenshiftRoutesCommand, ListOpenshiftRoutesUseCase (+21 more)

### Community 35 - "Screens / Session"
Cohesion: 0.09
Nodes (19): Changed, extract_requested_context(), is_context_command(), is_setup_command(), is_stack_command(), is_token_command(), format_context_switch_lines(), context_line() (+11 more)

### Community 36 - "Gitops / Azure"
Cohesion: 0.11
Nodes (25): _acquire_azure_token(), AzureMonitorMetricsAdapter, Client, MetricsQueryPort backed by Azure Monitor managed service for Prometheus.      Th, _acquire_google_token(), GCPManagedPrometheusAdapter, Client, MetricsQueryPort backed by GCP Managed Prometheus.      Managed Prometheus expos (+17 more)

### Community 37 - "Ports / Cluster"
Cohesion: 0.11
Nodes (29): ClusterDiffAdapter, ClusterInventorySource, Protocol, EmptyClusterInventorySource, ClusterDiffPort, ClusterInventoryData, ABC, TypedDict (+21 more)

### Community 38 - "Monthly / Use"
Cohesion: 0.09
Nodes (30): MonthlyIncidentAdapter, IncidentSnapshotData, MonthlyIncidentPort, ABC, TypedDict, ComputeMonthlyIncidentReportServicePort, ABC, ComputeMonthlyIncidentReportCommand (+22 more)

### Community 39 - "Memory / Duckdb"
Cohesion: 0.08
Nodes (41): purge(), command, option, Show the current DuckDB file size., Purge expired or old incidents from DuckDB., size(), format_size(), DuckDBUnavailableError (+33 more)

### Community 40 - "Hot / Services"
Cohesion: 0.12
Nodes (38): PodUsageRaw, TypedDict, _group_non_daemonset_pods(), HotNodeAnalysisUseCase, _node_series(), _to_consumer_dict(), _to_hot_node_dict(), _to_response() (+30 more)

### Community 41 - "Namespace / Services"
Cohesion: 0.08
Nodes (34): Fetch resource requests (K8s) and actual avg usage (Prometheus) for all namespac, DetectOverProvisionedNamespacesServicePort, ABC, DetectOverProvisionedNamespacesCommand, _any_actual_usage_present(), DetectOverProvisionedNamespacesUseCase, Orchestrates K8s+Prometheus data fetch and domain-level waste analysis., DetectOverProvisionedNamespacesResponse (+26 more)

### Community 42 - "Use / Case"
Cohesion: 0.10
Nodes (29): ContainerMetricsRecord, PodResourceMetricsPort, ABC, TypedDict, Outbound port — fetches pod resource usage and limits from the cluster., Return per-container CPU/memory usage and limits for *namespace*.          Raise, CheckResourceConstraintsServicePort, ABC (+21 more)

### Community 43 - "Use / Case"
Cohesion: 0.09
Nodes (29): TeamCostKubernetesAdapter, NamespaceResourceData, ABC, TypedDict, TeamCostPort, ComputeTeamCostServicePort, ABC, ComputeTeamCostCommand (+21 more)

### Community 44 - "Kubernetes / Ports"
Cohesion: 0.10
Nodes (25): _AppsApi, _build_edges_from_policies(), _CoreServiceApi, _items(), KubernetesTopologyAdapter, _match_services(), _NetworkingApi, Protocol (+17 more)

### Community 45 - "Adaptive / Use"
Cohesion: 0.12
Nodes (35): AdaptiveNamespaceInvestigationServicePort, ABC, AdaptiveNamespaceInvestigationUseCase, _to_candidate_dict(), _to_investigation_dict(), _to_overview_snapshot(), _to_response(), AdaptiveNamespaceInvestigationCommand (+27 more)

### Community 46 - "Pod / Use"
Cohesion: 0.11
Nodes (36): PodSecurityStandardsAuditCommand, _build_violation(), PodSecurityStandardsAuditUseCase, PodSecurityFindingDict, ViolationType, _scan_container(), _scan_pod(), _to_domain_container() (+28 more)

### Community 47 - "Ports / Gitops"
Cohesion: 0.10
Nodes (28): PredictionRoiAdapter, PredictionRoiSource, Protocol, _as_float(), ConfigPredictionRoiSource, PredictionRoiData, PredictionRoiPort, PreventedIncidentRaw (+20 more)

### Community 48 - "Ports / Services"
Cohesion: 0.10
Nodes (27): _build_uptime_query(), PrometheusReliabilityAdapter, IncidentRawData, ABC, TypedDict, ServiceReliabilityRawData, WeeklyReliabilityReportPort, GenerateWeeklyReliabilityReportServicePort (+19 more)

### Community 49 - "Pipeline / Ports"
Cohesion: 0.10
Nodes (30): PipelineRunRecord, TaskRunRecord, TektonPipelineBaselineAdapter, PipelineBaselinePort, PipelineRunRecord, ABC, TypedDict, List PipelineRuns filtered by pipeline label. (+22 more)

### Community 50 - "Image / Services"
Cohesion: 0.11
Nodes (32): ContainerImageDriftServicePort, ABC, ContainerImageDriftService, _find_matching(), _index_resolved_images(), ContainerImageDriftCommand, ContainerImageDriftResponse, _ResourceKey (+24 more)

### Community 51 - "Rbac / Services"
Cohesion: 0.11
Nodes (37): _RoleKey, AdaptiveInvestigationConstants, LogSearchConstants, QuotaConstants, Centralized constants for hexawyn — single source of truth.  All magic numbers,, Thresholds for pattern-based pod log search across all namespaces., Thresholds for semantic search and intent classification., Thresholds for adaptive namespace investigation drill-down. (+29 more)

### Community 52 - "Use / Case"
Cohesion: 0.10
Nodes (30): ContainerSecurityContextRaw, PodSecurityContextAuditPort, PodSecuritySpecRaw, ABC, TypedDict, Port for enumerating every Pod's security-relevant spec fields (pod-     and con, List every Pod across all namespaces with its raw security-context         field, Map namespace name to its `pod-security.kubernetes.io/enforce`         label val (+22 more)

### Community 53 - "Cost / Services"
Cohesion: 0.09
Nodes (30): CostSavingReport, EstimateCostSavingServicePort, ABC, EstimateCostSavingCommand, _compute_trend(), EstimateCostSavingUseCase, CostSavingReport, EstimateCostSavingResponse (+22 more)

### Community 54 - "License / Errors"
Cohesion: 0.07
Nodes (37): AmbiguousResultError, CheckerNodeError, HexawynError, InvestigationError, MutationGuardTriggeredError, Exception, Base exception for all hexawyn errors., Raised when the LangGraph investigation pipeline fails. (+29 more)

### Community 55 - "Services / Log"
Cohesion: 0.11
Nodes (28): ConnectionIssueCategory, _detect_level(), KubernetesPodLogWatchAdapter, _parse_line(), _parse_message(), Secondary adapter — live-tails pod logs via the Kubernetes watch API.      Recon, _split_timestamp(), PodLogWatchPort (+20 more)

### Community 56 - "Aws / Ports"
Cohesion: 0.12
Nodes (25): _all_values(), CloudWatchClient, CloudWatchClusterResourceMetricsAdapter, _find_result(), _GetMetricDataResponse, _latest_value(), _MetricDataResult, datetime (+17 more)

### Community 57 - "Gitops / Ports"
Cohesion: 0.11
Nodes (24): NightInterventionAdapter, NightInterventionSource, Protocol, EmptyNightInterventionSource, EngineerWorkloadPort, MonthNightData, ABC, TypedDict (+16 more)

### Community 58 - "Quota / Ports"
Cohesion: 0.10
Nodes (22): UsageMeterAdapter, ABC, Current consumption — read-only for display purposes., Current month's consumption for this resource., UsageMeterPort, GetQuotaUsageServicePort, ABC, GetQuotaUsageCommand (+14 more)

### Community 59 - "Rightsizing / Services"
Cohesion: 0.10
Nodes (31): EstimateRightsizingSavingsServicePort, ABC, EstimateRightsizingSavingsCommand, _any_actual_present(), EstimateRightsizingSavingsUseCase, EstimateRightsizingSavingsResponse, RightsizingRecommendation, RightsizingReport (+23 more)

### Community 60 - "Gitops / Ports"
Cohesion: 0.11
Nodes (23): BudgetIntelligenceAdapter, BudgetIntelligenceSource, Protocol, _as_float(), ConfigBudgetIntelligenceSource, BudgetIntelligenceData, BudgetIntelligencePort, ABC (+15 more)

### Community 61 - "Ports / Outdated"
Cohesion: 0.11
Nodes (24): HelmReleaseVersionAdapter, ChartLatestRawData, HelmReleaseRawData, HelmReleaseVersionPort, ABC, TypedDict, DetectOutdatedHelmReleasesServicePort, ABC (+16 more)

### Community 62 - "Gitops / Ports"
Cohesion: 0.12
Nodes (22): DisruptionRiskAdapter, DisruptionRiskSource, Protocol, EmptyDisruptionRiskSource, DisruptionRiskPort, ABC, TypedDict, RiskEventRaw (+14 more)

### Community 63 - "Ports / Kustomize"
Cohesion: 0.12
Nodes (23): KustomizeCLIPatchAdapter, BaseFieldRawData, KustomizePatchAnalysisPort, PatchFieldRawData, ABC, TypedDict, DetectKustomizePatchConflictsServicePort, ABC (+15 more)

### Community 64 - "Services / Event"
Cohesion: 0.11
Nodes (25): AnalyzeCriticalNamespaceEventsServicePort, ABC, AnalyzeCriticalNamespaceEventsUseCase, ECA-5 dependency: list_namespaces validates the namespace before fetching events, _to_response(), AnalyzeCriticalNamespaceEventsCommand, AnalyzeCriticalNamespaceEventsResponse, CriticalIncidentDict (+17 more)

### Community 65 - "Metrics / Use"
Cohesion: 0.11
Nodes (28): ExecutePrometheusQueryServicePort, ABC, ExecutePrometheusQueryCommand, ExecutePrometheusQueryUseCase, ExecutePrometheusQueryResponse, MetricResultDict, TypedDict, _to_response() (+20 more)

### Community 66 - "Certificate / Ports"
Cohesion: 0.11
Nodes (25): CertificateStatus, ClusterCertificateHealthPort, IngressRef, ABC, TypedDict, Outbound port — reads TLS secrets and ingresses from a Kubernetes cluster., TlsSecretData, _build_certificate_entry() (+17 more)

### Community 67 - "Gitops / Certificates"
Cohesion: 0.14
Nodes (15): CustomObjectsApi, CertManagerAdapter, CertManagerAdapter — queries real cert-manager CRDs via VanillaAdapter., Real cert-manager adapter using VanillaAdapter's CustomObjectsApi., CertManagerDetector, Auto-detects Cert-Manager via CRDs. All read-only — never triggers renewal., CertManagerNotFoundError, Raised when Cert-Manager is not installed in the cluster. (+7 more)

### Community 68 - "Datadog / Kubernetes"
Cohesion: 0.11
Nodes (24): _as_float(), _build_spans_api(), DatadogTracesAdapter, Exception, Protocol, Minimal contract for the Datadog v2 SpansApi used here., TraceQueryPort backed by Datadog APM (Spans API).      Reads slow spans and grou, _Span (+16 more)

### Community 69 - "Gitops / Ports"
Cohesion: 0.12
Nodes (21): CriticalCveAdapter, CriticalCveSource, Protocol, EmptyCriticalCveSource, CriticalCvePort, CveRaw, ABC, TypedDict (+13 more)

### Community 70 - "Gitops / Ports"
Cohesion: 0.12
Nodes (21): Protocol, StaleCredentialsAdapter, StaleCredentialsSource, EmptyStaleCredentialsSource, ABC, TypedDict, StaleCredentialRaw, StaleCredentialsPort (+13 more)

### Community 71 - "Gitops / Ports"
Cohesion: 0.12
Nodes (21): Protocol, UnauthorizedAccessAdapter, UnauthorizedAccessSource, EmptyUnauthorizedAccessSource, ABC, TypedDict, UnauthorizedAccessPort, UnauthorizedAccessRaw (+13 more)

### Community 72 - "Use / Case"
Cohesion: 0.12
Nodes (19): NamespaceEventsPort, ABC, GetNamespaceEventsServicePort, ABC, GetNamespaceEventsCommand, GetNamespaceEventsUseCase, to_response(), GetNamespaceEventsResponse (+11 more)

### Community 73 - "Use / Case"
Cohesion: 0.12
Nodes (28): AnalyzeFailedPipelineServicePort, ABC, AnalyzeFailedPipelineUseCase, AnalyzeFailedPipelineCommand, to_response(), AnalyzeFailedPipelineResponse, FailureAnalysisDict, TypedDict (+20 more)

### Community 74 - "Schedule / Commands"
Cohesion: 0.09
Nodes (34): create(), delete(), disable(), enable(), get(), history(), list(), argument (+26 more)

### Community 75 - "Canary / Ports"
Cohesion: 0.13
Nodes (21): OTelCanaryComparisonAdapter, VersionMetrics, CanaryComparisonPort, ABC, VersionMetrics, CanaryComparisonServicePort, ABC, CanaryComparisonUseCase (+13 more)

### Community 76 - "Ports / Use"
Cohesion: 0.12
Nodes (21): ServiceCostPrometheusAdapter, PodResourceSnapshotData, ABC, TypedDict, ServiceCostPort, CompareServiceCostServicePort, ABC, CompareServiceCostCommand (+13 more)

### Community 77 - "Resource / Ports"
Cohesion: 0.12
Nodes (17): KubernetesResourceYAMLAdapter, ABC, ResourceYAMLPort, ABC, ResourceYAMLCommand, ResourceYAMLResponse, ResourceYAMLServicePort, ResourceYamlCommand (+9 more)

### Community 78 - "Memory / Use"
Cohesion: 0.13
Nodes (20): PrometheusMemoryAdapter, MemorySaturationPort, ABC, MemorySaturationServicePort, ABC, MemorySaturationCommand, attach_otel_root_cause(), predictions_to_dicts() (+12 more)

### Community 79 - "Simulation / Services"
Cohesion: 0.12
Nodes (18): ABC, RunWhatIfSimulationServicePort, RunWhatIfSimulationCommand, RunWhatIfSimulationResponse, RunWhatIfSimulationUseCase, ImpactReport, RiskLevel, ScenarioInput (+10 more)

### Community 80 - "Gitops / Ports"
Cohesion: 0.11
Nodes (22): HelmDriftAdapter, _parse_multi_doc_yaml(), Secondary adapter — shells out to the `helm` CLI. Renders desired     state via, HelmValuesAdapter, Secondary adapter — reads effective Helm values via the `helm` CLI.      Uses ``, KustomizeDriftAdapter, _parse_multi_doc_yaml(), Secondary adapter — shells out to the `kustomize` CLI. `source` is a     local o (+14 more)

### Community 81 - "Version / Ports"
Cohesion: 0.14
Nodes (19): OTelVersionRegressionAdapter, VersionMetrics, ABC, VersionMetrics, VersionRegressionPort, ABC, VersionRegressionServicePort, VersionRegressionCommand (+11 more)

### Community 82 - "Ports / Gitops"
Cohesion: 0.12
Nodes (20): PolicyDetector, Auto-detects Kyverno vs OPA Gatekeeper via CRD presence. All read-only., PolicyPort, ABC, Port for policy engine (Kyverno / OPA Gatekeeper) operations — read-only., Detect Kyverno or Gatekeeper presence., Get a specific policy detail., List current violations. (+12 more)

### Community 83 - "Ports / Tls"
Cohesion: 0.13
Nodes (21): TLSComplianceAdapter, ABC, TypedDict, TLSCompliancePort, TLSServiceRawData, AuditTLSComplianceServicePort, ABC, AuditTLSComplianceUseCase (+13 more)

### Community 84 - "Ports / Use"
Cohesion: 0.11
Nodes (22): NamespacedPipelineRunInfo, ABC, TypedDict, Port for Tekton pipeline operations — read-only CRD access., List all TaskRuns for a pipeline.          Raises PipelineNotFoundError when the, List all PipelineRuns in a namespace (no pipeline name filter).          Returns, TektonPort, ListPipelineRunsInNamespaceServicePort (+14 more)

### Community 85 - "Log / Use"
Cohesion: 0.13
Nodes (27): DetectLogAnomaliesServicePort, ABC, DetectLogAnomaliesCommand, DetectLogAnomaliesUseCase, _to_response(), DetectLogAnomaliesResponse, LogAnomalyDict, TypedDict (+19 more)

### Community 86 - "Event / Services"
Cohesion: 0.13
Nodes (20): EventAnalysisConstants, Thresholds for Kubernetes event analysis and correlation., ClassifiedEvent, EventCategory, EventSeverity, Enum, Functional category of a Kubernetes event., A Kubernetes event with severity and category classification. (+12 more)

### Community 87 - "Deployment / Ports"
Cohesion: 0.15
Nodes (18): OTelDeploymentComparisonAdapter, DeploymentLatencyComparisonPort, ABC, DeploymentLatencyServicePort, ABC, DeploymentLatencyCommand, DeploymentLatencyUseCase, DeploymentLatencyResponse (+10 more)

### Community 88 - "Admin / Ports"
Cohesion: 0.14
Nodes (19): OTelSecurityAuditAdapter, ABC, SecurityAuditPort, AdminEndpointAuditServicePort, ABC, AdminEndpointAuditUseCase, AdminEndpointAuditCommand, AdminEndpointAuditResponse (+11 more)

### Community 89 - "Ports / Use"
Cohesion: 0.13
Nodes (20): RecurringIncidentAdapter, IncidentFrequencyData, ABC, TypedDict, RecurringIncidentPort, DetectRecurringIncidentsServicePort, ABC, DetectRecurringIncidentsCommand (+12 more)

### Community 90 - "Gitops / Errors"
Cohesion: 0.16
Nodes (14): GitOpsAdapter, GitOpsAdapter — queries real ArgoCD Applications via VanillaAdapter., Real GitOps adapter using VanillaAdapter's CustomObjectsApi for ArgoCD., GitOpsDetector, Auto-detects Flux CD or Argo CD by checking for CRDs in the cluster.      Delega, GitOpsEngineNotFoundError, Raised when no GitOps engine (Flux CD or Argo CD) is detected in the cluster., GitOpsApp (+6 more)

### Community 91 - "Tls / Ports"
Cohesion: 0.13
Nodes (17): KubernetesCertificateAdapter, CertificateInvestigationPort, ABC, ABC, TLSCertificateDiagnosisServicePort, TLSCertificateDiagnosisCommand, TLSCertificateDiagnosisResponse, TLSCertificateDiagnosisUseCase (+9 more)

### Community 92 - "Trace / Ports"
Cohesion: 0.15
Nodes (18): KubernetesEventAdapter, ABC, TraceEventCorrelationPort, ABC, TraceK8sEventsServicePort, TraceK8sEventsCommand, TraceK8sEventsResponse, TraceK8sEventsUseCase (+10 more)

### Community 93 - "Metric / Ports"
Cohesion: 0.15
Nodes (18): OTelPrometheusCorrelationAdapter, MetricCorrelationPort, ABC, MetricCorrelationServicePort, ABC, MetricCorrelationCommand, MetricCorrelationUseCase, MetricCorrelationResponse (+10 more)

### Community 94 - "Security / Ports"
Cohesion: 0.08
Nodes (16): PodSecurityProvider, Normalizes the Pod Security Standards audit into posture records.      The audit, Normalizes the TLS compliance audit into posture records.      A service whose s, TLSComplianceProvider, ComplianceCategoryProvider, Protocol, One security-audit category normalized into posture records.      Each provider, Facade over the individual security audits.      Fans out to each injected categ (+8 more)

### Community 95 - "Use / Case"
Cohesion: 0.12
Nodes (20): PipelineRunInfo, List all PipelineRuns for a service (pipeline name).          Raises ServiceNotF, ListPipelineRunsServicePort, ABC, ListPipelineRunsCommand, ListPipelineRunsUseCase, Fetches PipelineRuns, sorts, limits, computes stats and flags outliers., ListPipelineRunsResponse (+12 more)

### Community 96 - "Use / Case"
Cohesion: 0.12
Nodes (22): ABC, WatchPodLogsServicePort, WatchPodLogsCommand, TypedDict, WatchAlertDict, WatchPodLogsResponse, _count_occurrences(), _to_alert_dict() (+14 more)

### Community 97 - "Config / Kubernetes"
Cohesion: 0.14
Nodes (8): ClusterContext, DiscoveryService, FileKubernetesDiscoveryService, HexawynContextConfig, ABC, Path, Discover contexts from kubeconfig sources., Return Hexawyn preferred context or Kubernetes current context.

### Community 98 - "Aws"
Cohesion: 0.12
Nodes (19): AWSXRayTraceAdapter, _BatchGetTracesResponse, _chunked(), _duration_ms(), _GetTraceSummariesResponse, datetime, Protocol, TypedDict (+11 more)

### Community 99 - "Redundant / Ports"
Cohesion: 0.16
Nodes (19): OTelRedundantCallAdapter, ABC, RedundantCallDetectionPort, ABC, RedundantCallsServicePort, RedundantCallsCommand, RedundantCallsUseCase, RedundantCallsResponse (+11 more)

### Community 100 - "Tools / Custom"
Cohesion: 0.08
Nodes (17): Stream investigation results via SSE. Yields (node_name, output) tuples., RuntimeClient, custom_tool_describe(), FastMCP, MCP tool: custom_tool_describe — Show a custom tool's contract., Describe a custom tool: parameters, output schema, transport, endpoint., register(), custom_tool_run() (+9 more)

### Community 101 - "Error / Services"
Cohesion: 0.12
Nodes (21): ErrorBudgetPort, ABC, ComputeSLOErrorBudgetServicePort, ABC, ComputeSLOErrorBudgetCommand, ComputeSLOErrorBudgetUseCase, ComputeSLOErrorBudgetResponse, SLOErrorBudgetRequest (+13 more)

### Community 102 - "Ports / Rollouts"
Cohesion: 0.12
Nodes (19): ArgoRolloutsDetector, Detects Argo Rollouts by checking for CRDs and provides read-only access.      A, ABC, Port for Argo Rollouts operations — read-only., Detect if Argo Rollouts is installed and return summary counts., List all Rollouts with strategy and phase., Get detailed status of a specific Rollout., List AnalysisRuns, optionally filtered by rollout name. (+11 more)

### Community 103 - "Pipeline / Ports"
Cohesion: 0.16
Nodes (18): KubernetesPipelineRunLogsAdapter, PipelineRunLogsPort, ABC, PipelineRunLogsServicePort, ABC, PipelineRunLogsCommand, PipelineRunLogsUseCase, PipelineRunLogsResponse (+10 more)

### Community 104 - "Use / Case"
Cohesion: 0.12
Nodes (20): MTTRTrendAdapter, IncidentResolutionData, MTTRTrendPort, ABC, TypedDict, ComputeMTTRTrendServicePort, ABC, ComputeMTTRTrendCommand (+12 more)

### Community 105 - "Sensitive / Ports"
Cohesion: 0.16
Nodes (18): OTelComplianceAuditAdapter, ComplianceAuditPort, ABC, ABC, SensitiveDataAuditServicePort, SensitiveDataAuditCommand, SensitiveDataAuditResponse, SensitiveDataAuditUseCase (+10 more)

### Community 106 - "Cost / Ports"
Cohesion: 0.16
Nodes (17): OTelCostProfilingAdapter, CostProfilingPort, ABC, CostProfilingServicePort, ABC, CostProfilingCommand, CostProfilingUseCase, CostProfilingResponse (+9 more)

### Community 107 - "P99 / Ports"
Cohesion: 0.16
Nodes (18): OTelPrometheusLatencyAdapter, LatencyPercentilePort, ABC, P99LatencyServicePort, ABC, P99LatencyCommand, P99LatencyUseCase, P99LatencyResponse (+10 more)

### Community 108 - "Slowest / Ports"
Cohesion: 0.16
Nodes (18): OTelPodTraceAdapter, SlowTrace, ABC, SlowTrace, SlowTraceSearchPort, ABC, SlowestTracesServicePort, SlowestTracesCommand (+10 more)

### Community 109 - "Slo / Ports"
Cohesion: 0.14
Nodes (18): OTelSLOPredictionAdapter, ABC, SLOBreachPredictionPort, ABC, SLOBreachPredictionServicePort, SLOBreachPredictionCommand, SLOBreachPredictionResponse, SLOBreachPredictionUseCase (+10 more)

### Community 110 - "Use / Case"
Cohesion: 0.13
Nodes (21): PodMetricsBaselinePort, ABC, Driven port: provides current + 7-day-baseline CPU/memory/error-rate     usage f, Fetch baseline + current metrics for all pods in the namespace.          Returns, DetectPodAnomaliesServicePort, ABC, DetectPodAnomaliesCommand, DetectPodAnomaliesUseCase (+13 more)

### Community 111 - "Use / Case"
Cohesion: 0.16
Nodes (21): GenerateIncidentTriageReportServicePort, ABC, GenerateIncidentTriageReportCommand, GenerateIncidentTriageReportUseCase, _to_response(), _within_window(), GenerateIncidentTriageReportResponse, ImpactAssessmentDict (+13 more)

### Community 112 - "Etcd / Ports"
Cohesion: 0.16
Nodes (16): KubernetesETCDLogsAdapter, ETCDLogsPort, ABC, ETCDLogsServicePort, ABC, ETCDLogsCommand, ETCDLogsUseCase, ETCDLogsResponse (+8 more)

### Community 113 - "Gitops / Ports"
Cohesion: 0.19
Nodes (24): KubernetesRBACAdapter, _parse_audit_line(), Any, Exception, Secondary adapter — enumerates ServiceAccounts, RoleBindings/     ClusterRoleBin, _to_aggregation_selectors(), _to_binding(), _to_cluster_role() (+16 more)

### Community 114 - "Ports / Use"
Cohesion: 0.15
Nodes (17): OTelDependencyGraphAdapter, ABC, ServiceDependencyGraphPort, ABC, ServiceDependencyGraphServicePort, ServiceDependencyGraphCommand, ServiceDependencyGraphResponse, UseCaseDependencyGraphUseCase (+9 more)

### Community 115 - "Use / Case"
Cohesion: 0.14
Nodes (19): FleetHealthPort, ABC, Return all kubeconfig context names., GlobalHealthCheckServicePort, ABC, GlobalHealthCheckCommand, _compute_fleet_trend(), GlobalHealthCheckUseCase (+11 more)

### Community 116 - "Zombie / Services"
Cohesion: 0.15
Nodes (20): DetectZombiesServicePort, ABC, DetectZombiesCommand, DetectZombiesUseCase, DetectZombiesResponse, ZombieCandidate, ZombieDetectionResult, _as_bool() (+12 more)

### Community 117 - "Helm / Services"
Cohesion: 0.15
Nodes (20): DiffAgeProvider, HelmValuesDiffReport, ValueDiff, HelmValuesDiffService, DiffSeverity, Domain service — turns two Helm values trees into a graded diff report.      Enr, classify_severity(), _contains() (+12 more)

### Community 118 - "Gitops / Keda"
Cohesion: 0.18
Nodes (12): KedaAdapter, KedaAdapter — queries real KEDA CRDs via VanillaAdapter., Real KEDA adapter using VanillaAdapter's CustomObjectsApi., AuthType, HPAStatus, KedaScaledObject, KedaScaledObjectPhase, KedaTrigger (+4 more)

### Community 119 - "Pipeline / Ports"
Cohesion: 0.17
Nodes (16): KubernetesPipelineForServiceAdapter, PipelineForServicePort, ABC, PipelineForServiceServicePort, ABC, PipelineForServiceCommand, PipelineForUseCaseUseCase, PipelineForServiceResponse (+8 more)

### Community 120 - "Error / Ports"
Cohesion: 0.16
Nodes (16): OTelErrorAttributionAdapter, ErrorAttributionPort, ABC, ErrorAttributionServicePort, ABC, ErrorAttributionCommand, ErrorAttributionUseCase, ErrorAttributionResponse (+8 more)

### Community 121 - "Use / Case"
Cohesion: 0.18
Nodes (19): CompareClusterHealthServicePort, ABC, CompareClusterHealthCommand, CompareClusterHealthUseCase, _to_snapshot(), CompareClusterHealthResponse, ClusterHealthSnapshot, ComparisonReport (+11 more)

### Community 122 - "Use / Case"
Cohesion: 0.19
Nodes (23): index_bindings_by_service_account(), index_pods_by_service_account(), _RoleKey, _ServiceAccountKey, resolve_role(), to_candidate(), _to_finding_dict(), to_policy_rule() (+15 more)

### Community 123 - "Server / Config"
Cohesion: 0.15
Nodes (27): get_cache_stats(), DatadogConfig, get_datadog_config(), is_datadog_configured(), TypedDict, Read Datadog credentials and site from the environment., True when both Datadog keys are present in the environment., build_cluster_resource_metrics_adapter() (+19 more)

### Community 124 - "Headroom / Services"
Cohesion: 0.16
Nodes (24): BindingConstraint, HeadroomVerdict, HeadroomSimulationConstants, Thresholds for cluster headroom simulation of proposed workloads., ClusterHeadroomSnapshot, HeadroomSimulationReport, HeadroomSimulationRequest, ProposedWorkload (+16 more)

### Community 125 - "Stack / Presentation"
Cohesion: 0.15
Nodes (26): list_installed_providers(), CloudProvider, Return all installed CloudProvider classes (used by /config providers)., _aws_supported(), _azure_supported(), build_stack_lines(), _cluster_context(), _datadog_supported() (+18 more)

### Community 126 - "Ports / Gitops"
Cohesion: 0.15
Nodes (21): KubernetesAuditLogAdapter, _parse_audit_line(), Any, Exception, ManagedFieldsEntryRaw, Secondary adapter — enumerates ConfigMap/Secret managedFields (always     availa, _to_managed_fields_entry(), _to_resource() (+13 more)

### Community 127 - "Use / Case"
Cohesion: 0.15
Nodes (18): HeadroomSimulationPort, ABC, Driven port: node-allocatable totals, node count, and the largest     single nod, Fetches total allocatable CPU/memory, node count, the largest         single nod, ClusterHeadroomSimulationServicePort, ABC, ClusterHeadroomSimulationUseCase, _to_proposed_workload() (+10 more)

### Community 128 - "Schedule / Services"
Cohesion: 0.15
Nodes (10): ABC, Persistance des définitions de checks + historique des résultats., ScheduleStorePort, CheckResult, CronCheck, DuckDBScheduleStore, DuckDBPyConnection, Persiste définitions + historique dans DuckDB. (+2 more)

### Community 129 - "Services / Event"
Cohesion: 0.20
Nodes (24): AdvancedEventAnalyticsConstants, Thresholds for the 6h advanced namespace event analytics report (ECA-19/ECA-20)., NamespaceEvent, AdvancedEventAnalyticsReport, _build_timeline(), generate_advanced_event_analytics(), IncidentSummary, _parse_timestamp() (+16 more)

### Community 130 - "Pod / Services"
Cohesion: 0.14
Nodes (25): AnomalyPoint, PodMetricsRawData, TypedDict, Raw per-pod CPU/memory/error-rate baseline + current usage — one entry     per p, PodAnomalyDetectionConstants, Thresholds for pod metrics anomaly detection vs 7-day baseline     (Z-score + Is, ExcludedPod, PodAnomaly (+17 more)

### Community 131 - "Ports / Use"
Cohesion: 0.15
Nodes (16): HelmReleaseValues, HelmValuesDiffPort, ABC, TypedDict, Driven port — retrieves the effective Helm values for a release.      "Effective, Return the effective values for *release* in *namespace*.          Raises HelmNo, DiffHelmValuesServicePort, ABC (+8 more)

### Community 132 - "Anonymization / Logging"
Cohesion: 0.19
Nodes (18): AnonymizerPort, ABC, Anonymizer port — mask/unmask sensitive data for external destinations., AnonymizationMap, Destination, Enum, Anonymization domain models — SensitiveMatch, AnonymizationMap, policies., RedactionPolicy (+10 more)

### Community 133 - "Usage / Monitoring"
Cohesion: 0.20
Nodes (15): ABC, UsageLedgerPort, DailyStats, InvestigationUsage, MonthlyReport, TypedDict, ToolStat, UsageStats (+7 more)

### Community 134 - "Ports / Gitops"
Cohesion: 0.14
Nodes (9): KedaDetector, Auto-detects KEDA via CRDs. All read-only — never triggers scale., KedaPort, ABC, Port for KEDA operations — read-only. Never triggers scale., KedaNotFoundError, Raised when KEDA is not installed in the cluster., KedaDetectionResult (+1 more)

### Community 135 - "Gitops / Ports"
Cohesion: 0.15
Nodes (19): _cpu_to_cores(), _fetch_pod_metrics(), _float_prefix(), _is_daemonset(), KubernetesNodeAnalysisAdapter, _memory_to_bytes(), _node_allocatable(), _node_allocatable_cpu() (+11 more)

### Community 136 - "Cluster / Use"
Cohesion: 0.20
Nodes (21): Confidence, CriticalResource, ClusterCapacityCeilingForecastUseCase, _to_resource_dict(), _to_response(), TypedDict, ResourceForecastDict, InsufficientDataError (+13 more)

### Community 137 - "Ports / Openshift"
Cohesion: 0.12
Nodes (11): _build_success_rate_query(), PrometheusErrorBudgetAdapter, OpenShiftMonitoringAdapter, MetricsQueryPort backed by the built-in OpenShift Monitoring stack.      OpenShi, TypedDict, ServiceSuccessRateRawData, MetricsQueryPort, ABC (+3 more)

### Community 138 - "Schedule / Services"
Cohesion: 0.13
Nodes (14): AlertNotificationPort, ABC, Format a cluster finding into a generic AlertMessage.         Each adapter rende, CheckPhase, NotifyPolicy, Enum, str, ScheduleStatus (+6 more)

### Community 139 - "Topology / Services"
Cohesion: 0.15
Nodes (17): ABC, Persist a topology snapshot for historical comparison.          Best-effort: imp, TopologySnapshotPort, DependencyGraph, DependencyEdgeExport, DependencyGraphExport, DependencyGraph, TypedDict (+9 more)

### Community 140 - "Spike / Services"
Cohesion: 0.17
Nodes (18): ClusterCapacitySnapshot, SpikeProvisioningReport, _binding_constraint(), DemandProjection, project_demand(), Project peak CPU/memory utilisation under a traffic multiplier.      The binding, _utilization(), NodeRecommendation (+10 more)

### Community 141 - "Datadog"
Cohesion: 0.17
Nodes (16): _build_metrics_api(), DatadogClusterResourceMetricsAdapter, _host_from_scope(), _latest_value(), MetricsApi, datetime, Exception, Protocol (+8 more)

### Community 142 - "Istio / Ports"
Cohesion: 0.13
Nodes (14): _get_failing_pipelines(), _build_edges_from_virtual_services(), _CustomObjectsApi, IstioTopologyAdapter, _items(), _primary_host(), Protocol, IstioTopologyAdapter — infers edges from Istio VirtualService CRDs (best-effort) (+6 more)

### Community 143 - "Gitops / Ports"
Cohesion: 0.16
Nodes (19): _cpu_to_cores(), _detect_autoscaler(), _float_prefix(), KubernetesCapacityForecastAdapter, _memory_to_bytes(), _node_allocatable(), _node_allocatable_cpu(), _node_allocatable_memory_gb() (+11 more)

### Community 144 - "Slack / Commands"
Cohesion: 0.14
Nodes (16): POST to a Slack API method (e.g. 'chat.postMessage').         Returns the parsed, Low-level HTTP client for the Slack Web API. Injectable into secondary adapters., SlackHttpClient, Posts messages to Slack via chat.postMessage using SLACK_BOT_TOKEN.     SlackHtt, SlackHttpPublisher, listen(), command, option (+8 more)

### Community 145 - "Ports / Tools"
Cohesion: 0.11
Nodes (16): ABC, Port for enumerating ServiceAccounts, their RoleBindings/     ClusterRoleBinding, List every ServiceAccount across all namespaces., List every ClusterRoleBinding and RoleBinding across all namespaces., List every Role and ClusterRole, including own labels and raw         aggregatio, List every Pod's owning service account, across all namespaces., Fetch k8s audit log events for service-account API calls, if configured., RBACSecurityAuditPort (+8 more)

### Community 146 - "Use / Case"
Cohesion: 0.20
Nodes (17): AnalyzePodLogsServicePort, ABC, AnalyzePodLogsUseCase, _to_connection_issue_dict(), _to_response(), AnalyzePodLogsCommand, AnalyzePodLogsResponse, ConnectionIssueDict (+9 more)

### Community 147 - "Use / Case"
Cohesion: 0.16
Nodes (14): ListPodsServicePort, ABC, ListPodsCommand, List pods in namespace — use case., ListPodsUseCase, Lists pods in a namespace, sorted unhealthy first., ListPodsResponse, _sort_key() (+6 more)

### Community 148 - "Use / Case"
Cohesion: 0.17
Nodes (16): ABC, SummarizeNamespaceEventsServicePort, SummarizeNamespaceEventsCommand, SummarizeNamespaceEventsResponse, ECA-5 dependency: list_namespaces validates the namespace before fetching events, SummarizeNamespaceEventsUseCase, _to_response(), NamespaceEventsSummary (+8 more)

### Community 149 - "Incident / Services"
Cohesion: 0.21
Nodes (21): ImpactAssessment, IncidentCauseCategory, IncidentTriageRequest, Enum, Functional category of an incident's likely root cause., One reconstructed event in the incident timeline., TimelineEntry, _build_all_entries() (+13 more)

### Community 150 - "Configuration / Services"
Cohesion: 0.20
Nodes (19): DriftSeverity, ConfigurationDriftRequest, DriftedField, ResourceManifest, classify_severity(), RBAC/Secret kinds are always critical regardless of which field     drifted; oth, compare_dict_field(), compare_scalar_field() (+11 more)

### Community 151 - "Azure"
Cohesion: 0.13
Nodes (8): AzureAKSAdapter, ClusterContext, K8sPort implementation for Azure AKS.      Kubernetes reads are delegated to an, Fetch live AKS cluster metadata.          Raises ClusterUnreachableError when cr, AzureAKSProvider, CloudProvider, ClusterContext, CloudProvider plugin for Azure AKS clusters.      Selected automatically by the

### Community 152 - "Datadog / Ports"
Cohesion: 0.15
Nodes (14): _build_monitors_api(), DatadogMonitorAdapter, _Monitor, MonitorsApi, Protocol, Minimal contract for the Datadog v1 MonitorsApi used here., MonitoringPort backed by Datadog Monitors API.      Reads active Datadog monitor, MonitoringPort (+6 more)

### Community 153 - "Optimization / Services"
Cohesion: 0.19
Nodes (18): OptimizationRaw, PerformanceMetricRaw, OptimizationItem, OptimizationRoiReport, PerformanceImpact, analyze_performance(), has_regression(), _higher_is_better() (+10 more)

### Community 154 - "License / Screens"
Cohesion: 0.15
Nodes (15): format_license_aside_lines(), format_license_footer_hint(), ComposeResult, ComposeResult, _get_current_plan(), ComposeResult, Read current license plan from ~/.hexawyn/license.key if it exists., LicenseClaims (+7 more)

### Community 155 - "Cache / Memory"
Cohesion: 0.13
Nodes (10): CacheEntry, True if entry is within TTL window., Age of entry in seconds., A Cache L1 entry — exact match by query hash.     TTL: 5 minutes (CACHE_TTL_SECO, compute_query_hash(), get_l1(), invalidate_l1(), set_l1() (+2 more)

### Community 156 - "Ports / Gitops"
Cohesion: 0.16
Nodes (13): Provides cluster capacity for spike planning.      Reuses the headroom port for, SpikeProvisioningAdapter, ClusterCapacityRaw, ABC, TypedDict, Driven port — provides current cluster capacity and optional history for     spi, Fetch current node count, allocatable/used CPU and memory, and         whether a, Return last year's observed peak traffic multiplier for this event,         or N (+5 more)

### Community 157 - "Ports / Container"
Cohesion: 0.14
Nodes (15): ImageDriftPort, ABC, TypedDict, Port for resolving each running container's actually-pulled image     digest (ku, List every container's resolved imageID, joined to its owning         Deployment, ResolvedContainerImageRaw, DetectContainerImageDriftCommand, DetectContainerImageDriftUseCase (+7 more)

### Community 158 - "Use / Case"
Cohesion: 0.18
Nodes (14): LiveTopologyMapperServicePort, ABC, LiveTopologyMapperCommand, LiveTopologyMapperUseCase, LiveTopologyMapperResponse, DependencyGraph, build_istio_topology_adapter(), build_kubernetes_topology_adapter() (+6 more)

### Community 159 - "Security / Services"
Cohesion: 0.23
Nodes (17): CategoryScore, TypedDict, SecurityPostureReport, WorkloadCompliance, WorkloadComplianceRaw, _category_score_pct(), compute_overall_score(), Score one compliance category.      Exempt workloads are excluded from the denom (+9 more)

### Community 160 - "Aws"
Cohesion: 0.15
Nodes (11): CloudWatchLogsAdapter, _error_code(), _FilterLogEventsResponse, LogsClient, _parse_message(), Exception, Protocol, TypedDict (+3 more)

### Community 161 - "Fleet / Config"
Cohesion: 0.16
Nodes (16): FleetHealthAdapter, _get_cert_counts(), _get_node_counts(), _get_pod_counts(), _get_resource_utilization(), _get_security_violations(), _items(), _node_ready() (+8 more)

### Community 162 - "Gitops / Ports"
Cohesion: 0.17
Nodes (13): OptimizationRoiAdapter, Protocol, Assembles a sprint's ROI inputs from the cost, right-sizing and     reliability, Facade over the cost / right-sizing / reliability sources.      Delegates to an, SprintRoiSource, EmptySprintRoiSource, Default sprint ROI source used until a persistent sprint baseline store     is w, OptimizationRoiPort (+5 more)

### Community 163 - "Slack / Ports"
Cohesion: 0.17
Nodes (11): Sends alerts to Slack via incoming webhook.     Free tier: 5 alerts/month (quota, Send a connectivity test without consuming quota., SlackAlertAdapter, AlertMessage, TypedDict, Send an alert message to the notification platform.         Returns True if sent, A Slack message to be sent via webhook.     Free tier (is_pro_format=False): bas, SlackBlock (+3 more)

### Community 164 - "Ports / Memory"
Cohesion: 0.13
Nodes (12): CachePort, CacheStatsDict, ABC, Return cached result with validation against current pod state., Store a sanitized investigation result., Invalidate a specific cache entry., Invalidate all entries for a given resource., Delete all cache entries (RGPD right to erasure). (+4 more)

### Community 165 - "Use / Case"
Cohesion: 0.19
Nodes (13): AdvancedNamespaceEventAnalyticsServicePort, ABC, AdvancedNamespaceEventAnalyticsResponse, AdvancedNamespaceEventAnalyticsUseCase, AdvancedNamespaceEventAnalyticsResponse, ECA-5 dependency: list_namespaces validates the namespace before fetching events, _to_response(), AdvancedNamespaceEventAnalyticsCommand (+5 more)

### Community 166 - "Use / Case"
Cohesion: 0.18
Nodes (12): ListNamespacesServicePort, ABC, ListNamespacesCommand, List namespaces — use case., ListNamespacesUseCase, Lists all namespaces and their age from the K8s API., ListNamespacesResponse, list_namespaces() (+4 more)

### Community 167 - "Errors / Historicaldatawindowexpirederror"
Cohesion: 0.10
Nodes (4): HistoricalDataWindowExpiredError, Raised when the monthly Slack alert limit is reached.     Limits by tier:     -, Raised when the requested timestamp predates KubeArchive's data retention window, SlackQuotaExceededError

### Community 168 - "Services / Failure"
Cohesion: 0.18
Nodes (10): Thresholds for RCA confidence scoring and impact assessment., ScoringConstants, FailureImpactScore, Confidence score for a root cause analysis., Impact score of a failure on the system., Configurable weights and thresholds for RCA scoring.      All weights are additi, RcaConfidenceScore, RcaScoringConfig (+2 more)

### Community 169 - "Gitops / Ports"
Cohesion: 0.19
Nodes (12): _extract_container_status(), KubernetesAdaptiveInvestigationAdapter, CoreV1Api, Exception, Secondary adapter — drills into a single failing resource: events,     container, _translate_error(), AdaptiveInvestigationPort, ABC (+4 more)

### Community 170 - "Use / Case"
Cohesion: 0.19
Nodes (12): ForecastCostServicePort, ABC, ForecastCostCommand, ForecastCostUseCase, CostDriver, CostForecastResult, ForecastCostResponse, forecast_cost() (+4 more)

### Community 171 - "Use / Case"
Cohesion: 0.17
Nodes (12): GitOpsAppStatusServicePort, ABC, GitOpsAppStatusCommand, GitOpsAppStatusResponse, GitopsAppStatusCommand, GitopsAppStatusUseCase, GitopsAppStatusResponse, build_gitops_adapter() (+4 more)

### Community 172 - "Use / Case"
Cohesion: 0.16
Nodes (12): KedaScaledObjectTriggersServicePort, ABC, KedaScaledObjectTriggersCommand, KedaScaledObjectTriggersResponse, KedaScaledobjectTriggersCommand, KedaScaledobjectTriggersUseCase, KedaScaledobjectTriggersResponse, build_keda_adapter() (+4 more)

### Community 173 - "Use / Case"
Cohesion: 0.20
Nodes (11): LatencyDiagnosticServicePort, ABC, LatencyDiagnosticCommand, LatencyDiagnosticUseCase, LatencyDiagnosticResponse, LatencyDiagnosticResult, SpanBreakdown, latency_diagnostic() (+3 more)

### Community 174 - "Use / Case"
Cohesion: 0.21
Nodes (12): ListTaskRunsServicePort, ABC, ListTaskRunsCommand, ListTaskRunsUseCase, Lists TaskRuns for a pipeline, sorted by start time descending., ListTaskRunsResponse, sort_by_start_time_desc(), _start_time_sort_key() (+4 more)

### Community 175 - "Gcp / Ports"
Cohesion: 0.27
Nodes (7): GCPCloudTraceAdapter, TraceQueryPort backed by Google Cloud Trace (v1 read API).      Fetches slow tra, OTelHTTPAdapter, ABC, TraceQueryPort, LatencyDiagnosticRequest, TraceSpan

### Community 176 - "Ports / Use"
Cohesion: 0.11
Nodes (10): CertManagerPort, ABC, Port for Cert-Manager operations — read-only. Never triggers renewal., Detect Cert-Manager presence., List all certificates., Get a specific certificate., List Issuers and ClusterIssuers., Get a specific Issuer. (+2 more)

### Community 177 - "Use / Case"
Cohesion: 0.22
Nodes (11): ComputeOptimizationRoiServicePort, ABC, ComputeOptimizationRoiCommand, ComputeOptimizationRoiUseCase, ComputeOptimizationRoiResponse, OptimizationRoiService, Domain service — turns before/after sprint data into a ROI report:     monthly a, compute_optimization_roi() (+3 more)

### Community 178 - "Use / Case"
Cohesion: 0.18
Nodes (12): GitOpsAppGetServicePort, ABC, GitOpsAppGetCommand, GitOpsAppGetResponse, GitopsAppGetCommand, GitopsAppGetUseCase, GitopsAppGetResponse, gitops_app_get() (+4 more)

### Community 179 - "Use / Case"
Cohesion: 0.18
Nodes (11): GitOpsAppsListServicePort, ABC, GitOpsAppsListCommand, GitOpsAppsListResponse, GitopsAppsListCommand, GitopsAppsListUseCase, GitopsAppsListResponse, gitops_apps_list() (+3 more)

### Community 180 - "Use / Case"
Cohesion: 0.18
Nodes (11): GitOpsDetectServicePort, ABC, GitOpsDetectCommand, GitOpsDetectResponse, GitopsDetectCommand, GitopsDetectUseCase, GitopsDetectResponse, gitops_detect() (+3 more)

### Community 181 - "Use / Case"
Cohesion: 0.17
Nodes (10): KedaScaledJobGetServicePort, ABC, KedaScaledJobGetCommand, KedaScaledJobGetResponse, KedaScaledjobGetCommand, KedaScaledjobGetUseCase, KedaScaledjobGetResponse, keda_scaledjob_get() (+2 more)

### Community 182 - "Use / Case"
Cohesion: 0.17
Nodes (11): KedaScaledJobsListServicePort, ABC, KedaScaledJobsListCommand, KedaScaledJobsListResponse, KedaScaledjobsListCommand, KedaScaledjobsListUseCase, KedaScaledjobsListResponse, keda_scaledjobs_list() (+3 more)

### Community 183 - "Use / Case"
Cohesion: 0.18
Nodes (10): KedaScaledObjectGetServicePort, ABC, KedaScaledObjectGetCommand, KedaScaledObjectGetResponse, KedaScaledobjectGetCommand, KedaScaledobjectGetUseCase, KedaScaledobjectGetResponse, keda_scaledobject_get() (+2 more)

### Community 184 - "Use / Case"
Cohesion: 0.17
Nodes (11): KedaScaledObjectStatusServicePort, ABC, KedaScaledObjectStatusCommand, KedaScaledObjectStatusResponse, KedaScaledobjectStatusCommand, KedaScaledobjectStatusUseCase, KedaScaledobjectStatusResponse, keda_scaledobject_status() (+3 more)

### Community 185 - "Use / Case"
Cohesion: 0.17
Nodes (11): KedaScaledObjectsListServicePort, ABC, KedaScaledObjectsListCommand, KedaScaledObjectsListResponse, KedaScaledobjectsListCommand, KedaScaledobjectsListUseCase, KedaScaledobjectsListResponse, keda_scaledobjects_list() (+3 more)

### Community 186 - "Use / Case"
Cohesion: 0.17
Nodes (10): KedaTriggerAuthGetServicePort, ABC, KedaTriggerAuthGetCommand, KedaTriggerAuthGetResponse, KedaTriggerauthGetCommand, KedaTriggerauthGetUseCase, KedaTriggerauthGetResponse, keda_triggerauth_get() (+2 more)

### Community 187 - "Use / Case"
Cohesion: 0.17
Nodes (11): KedaTriggerAuthListServicePort, ABC, KedaTriggerAuthListCommand, KedaTriggerAuthListResponse, KedaTriggerauthListCommand, KedaTriggerauthListUseCase, KedaTriggerauthListResponse, keda_triggerauth_list() (+3 more)

### Community 188 - "Services / Anomaly"
Cohesion: 0.17
Nodes (12): LogAnomalyDetectionConstants, Thresholds for statistical + ML log anomaly detection (ECA-14)., _extract_latency_ms(), extract_log_features(), Pure numeric feature vector for a single log line.      No NLP/embeddings — leng, IsolationForestAnomalyDetector, MLAnomalyDetectionResult, Output of an Isolation Forest semantic anomaly detection run. (+4 more)

### Community 189 - "Use / Case"
Cohesion: 0.24
Nodes (8): Primary adapter for Slack Chat.     Receives Slack messages, delegates to ChatSl, SlackChatAdapter, ChatSlackCommand, ChatSlackResponse, ChatSlackUseCase, Orchestrates Slack chat investigations via RuntimePort.     Never catches except, QuotaExceededError, Raised when the monthly investigation limit is reached.     Limits by tier:

### Community 190 - "Slack / Ports"
Cohesion: 0.15
Nodes (10): _get_active_cluster_name(), Primary adapter — HTTP server that receives Slack Events API webhooks.      Hand, Route a Slack event. Pure function — testable without HTTP., Start the HTTP server. Blocking — run from a dedicated process., SlackEventServer, MessagePublisherPort, ABC, Post a message to a channel.         Returns the message timestamp if delivered, (+2 more)

### Community 191 - "Azure"
Cohesion: 0.22
Nodes (9): _as_float(), AzureMonitorTracesAdapter, LogsClient, _LogsResult, _LogsTable, Protocol, Minimal contract for the azure-monitor-query LogsQueryClient used here., TraceQueryPort backed by Azure Monitor (Application Insights) via KQL.      Read (+1 more)

### Community 192 - "Memory / Duckdb"
Cohesion: 0.17
Nodes (5): Return cached result if valid (not expired), otherwise None., CachedInvestigation, A sanitized investigation result stored in local DuckDB., DuckDBCacheAdapter, Investigation cache backed by DuckDB. Lives in ~/.hexawyn/cache.db.

### Community 193 - "Ports / Use"
Cohesion: 0.15
Nodes (9): NetworkPolicyAuditPort, ABC, Port for enumerating every namespace (with its pod count) and every     NetworkP, List every namespace with its live pod count (0 if empty)., True if any Calico GlobalNetworkPolicy CRD exists in the cluster., True if any Istio PeerAuthentication with mTLS mode STRICT exists., EastWestNetworkSegmentationCommand, EastWestNetworkSegmentationUseCase (+1 more)

### Community 194 - "Use / Case"
Cohesion: 0.23
Nodes (10): DetectMissingProbesServicePort, ABC, DetectMissingProbesCommand, DetectMissingProbesUseCase, DetectMissingProbesResponse, build_optimization_roi_adapter(), detect_missing_probes(), FastMCP (+2 more)

### Community 195 - "Use / Case"
Cohesion: 0.23
Nodes (11): DetectNetworkSegmentationGapsServicePort, ABC, DetectNetworkSegmentationGapsCommand, DetectNetworkSegmentationGapsUseCase, DetectNetworkSegmentationGapsResponse, build_network_policy_audit_adapter(), detect_network_segmentation_gaps(), FastMCP (+3 more)

### Community 196 - "Use / Case"
Cohesion: 0.20
Nodes (11): GitOpsAppSyncServicePort, ABC, GitOpsAppSyncCommand, GitOpsAppSyncResponse, GitopsAppSyncCommand, GitopsAppSyncUseCase, GitopsAppSyncResponse, gitops_app_sync() (+3 more)

### Community 197 - "Use / Case"
Cohesion: 0.20
Nodes (11): GitOpsSourceGetServicePort, ABC, GitOpsSourceGetCommand, GitOpsSourceGetResponse, GitopsSourceGetCommand, GitopsSourceGetUseCase, GitopsSourceGetResponse, gitops_source_get() (+3 more)

### Community 198 - "Use / Case"
Cohesion: 0.20
Nodes (11): GitOpsSourcesListServicePort, ABC, GitOpsSourcesListCommand, GitOpsSourcesListResponse, GitopsSourcesListCommand, GitopsSourcesListUseCase, GitopsSourcesListResponse, gitops_sources_list() (+3 more)

### Community 199 - "Use / Case"
Cohesion: 0.22
Nodes (10): PolicyAuditServicePort, ABC, PolicyAuditCommand, PolicyAuditUseCase, PolicyAuditResponse, policy_audit(), FastMCP, MCP tool: policy_audit — Global compliance audit report. (+2 more)

### Community 200 - "Use / Case"
Cohesion: 0.23
Nodes (10): PolicyGetServicePort, ABC, PolicyGetCommand, PolicyGetUseCase, PolicyGetResponse, build_policy_adapter(), policy_get(), FastMCP (+2 more)

### Community 201 - "Use / Case"
Cohesion: 0.23
Nodes (10): ABC, RolloutsDetectServicePort, RolloutsDetectCommand, RolloutsDetectResponse, RolloutsDetectUseCase, build_rollouts_adapter(), FastMCP, MCP tool: rollouts_detect. (+2 more)

### Community 202 - "Services / Topology"
Cohesion: 0.31
Nodes (15): DependencyEdge, InferenceSource, NodeType, Enum, ServiceNode, _build_node(), _count_degree(), _detect_cycles() (+7 more)

### Community 203 - "Fleet / Services"
Cohesion: 0.32
Nodes (14): Collect raw metrics for a single cluster context.         Raises ClusterUnreacha, CategoryReport, ClusterRawMetrics, build_categories(), build_cluster_report(), _cert_category(), compute_health_score(), _cpu_category() (+6 more)

### Community 204 - "Ports / Use"
Cohesion: 0.12
Nodes (8): GitOpsPort, ABC, Port for GitOps engine (Flux CD / Argo CD) operations — read-only., Auto-detect Flux CD or Argo CD in the cluster., List all GitOps applications (HelmRelease, Kustomization, Application)., Get detailed status of a specific GitOps application., List GitOps sources (GitRepository, HelmRepository, Bucket)., Get detailed status of a specific GitOps source.

### Community 205 - "Use / Case"
Cohesion: 0.28
Nodes (10): CertsChallengesListServicePort, ABC, CertsChallengesListUseCase, CertsChallengesListCommand, CertsChallengesListResponse, build_cert_manager_adapter(), certs_challenges_list(), FastMCP (+2 more)

### Community 206 - "Use / Case"
Cohesion: 0.24
Nodes (9): CertsDetectServicePort, ABC, CertsDetectUseCase, CertsDetectCommand, CertsDetectResponse, certs_detect(), FastMCP, MCP tool: certs_detect — Detect if Cert-Manager is installed. (+1 more)

### Community 207 - "Use / Case"
Cohesion: 0.24
Nodes (9): CertsGetServicePort, ABC, CertsGetUseCase, CertsGetCommand, CertsGetResponse, certs_get(), FastMCP, MCP tool: certs_get — Get detailed status of a specific certificate. (+1 more)

### Community 208 - "Use / Case"
Cohesion: 0.24
Nodes (9): CertsIssuerGetServicePort, ABC, CertsIssuerGetUseCase, CertsIssuerGetCommand, CertsIssuerGetResponse, certs_issuer_get(), FastMCP, MCP tool: certs_issuer_get — Get detail of a specific Issuer. (+1 more)

### Community 209 - "Use / Case"
Cohesion: 0.24
Nodes (9): CertsIssuersListServicePort, ABC, CertsIssuersListUseCase, CertsIssuersListCommand, CertsIssuersListResponse, certs_issuers_list(), FastMCP, MCP tool: certs_issuers_list — List all Issuers. (+1 more)

### Community 210 - "Use / Case"
Cohesion: 0.24
Nodes (9): CertsRequestsListServicePort, ABC, CertsRequestsListUseCase, CertsRequestsListCommand, CertsRequestsListResponse, certs_requests_list(), FastMCP, MCP tool: certs_requests_list — List recent CertificateRequests. (+1 more)

### Community 211 - "Use / Case"
Cohesion: 0.24
Nodes (9): CertsStatusExplainServicePort, ABC, CertsStatusExplainUseCase, CertsStatusExplainCommand, CertsStatusExplainResponse, certs_status_explain(), FastMCP, MCP tool: certs_status_explain — Explain in natural language why a cert is faili (+1 more)

### Community 212 - "Use / Case"
Cohesion: 0.24
Nodes (9): CheckClusterCertificateHealthServicePort, ABC, CheckClusterCertificateHealthUseCase, CheckClusterCertificateHealthCommand, CheckClusterCertificateHealthResponse, check_cluster_certificate_health(), FastMCP, MCP tool: check_cluster_certificate_health. (+1 more)

### Community 213 - "Use / Case"
Cohesion: 0.24
Nodes (9): ComputeSecurityPostureServicePort, ABC, ComputeSecurityPostureCommand, ComputeSecurityPostureUseCase, ComputeSecurityPostureResponse, compute_security_posture(), FastMCP, MCP tool: compute_security_posture. (+1 more)

### Community 214 - "Use / Case"
Cohesion: 0.24
Nodes (9): KedaDetectServicePort, ABC, KedaDetectCommand, KedaDetectUseCase, KedaDetectResponse, keda_detect(), FastMCP, MCP tool: keda_detect — Detect if KEDA is installed. (+1 more)

### Community 215 - "Use / Case"
Cohesion: 0.24
Nodes (9): PolicyDetectServicePort, ABC, PolicyDetectCommand, PolicyDetectUseCase, PolicyDetectResponse, policy_detect(), FastMCP, MCP tool: policy_detect. (+1 more)

### Community 216 - "Use / Case"
Cohesion: 0.24
Nodes (9): PolicyListServicePort, ABC, PolicyListCommand, PolicyListUseCase, PolicyListResponse, policy_list(), FastMCP, MCP tool: policy_list. (+1 more)

### Community 217 - "Use / Case"
Cohesion: 0.24
Nodes (9): PolicyViolationsListServicePort, ABC, PolicyViolationsListCommand, PolicyViolationsListUseCase, PolicyViolationsListResponse, policy_violations_list(), FastMCP, MCP tool: policy_violations_list. (+1 more)

### Community 218 - "Use / Case"
Cohesion: 0.24
Nodes (10): ABC, RolloutGetServicePort, RolloutGetCommand, RolloutGetResponse, RolloutGetUseCase, FastMCP, MCP tool: rollout_get — Get detailed status of a specific Rollout., Get detailed status of a specific Argo Rollout with step information.      Args: (+2 more)

### Community 219 - "Use / Case"
Cohesion: 0.24
Nodes (9): ABC, RolloutStatusServicePort, RolloutStatusCommand, RolloutStatusResponse, RolloutStatusUseCase, FastMCP, MCP tool: rollout_status., register() (+1 more)

### Community 220 - "Use / Case"
Cohesion: 0.24
Nodes (9): ABC, RolloutsListServicePort, RolloutsListCommand, RolloutsListResponse, RolloutsListUseCase, FastMCP, MCP tool: rollouts_list — List all Argo Rollouts., register() (+1 more)

### Community 221 - "Use / Case"
Cohesion: 0.18
Nodes (12): IncidentSummary, _to_incident_dict(), _to_sample_event_dict(), AnalyzeAdvancedNamespaceEventsUseCase, AnalyzeAdvancedNamespaceEventsCommand, AdvancedNamespaceEventAnalyticsResponse, AnalyzeAdvancedNamespaceEventsResponse, EventStormDict (+4 more)

### Community 222 - "Gitops / Ports"
Cohesion: 0.25
Nodes (14): _cpu_to_cores(), _detect_autoscaler(), _float_prefix(), KubernetesHeadroomSimulationAdapter, _memory_to_bytes(), _node_allocatable(), _node_allocatable_cpu(), _node_allocatable_memory_gb() (+6 more)

### Community 223 - "Ports / Pricing"
Cohesion: 0.16
Nodes (8): PricingPlanAdapter, PlanPort, ABC, Is the feature available in the current plan?, Minimum tier required to unlock this feature., Source of quotas — reflects the Pricing Matrix (Notion)., Return the limit for a resource. None = unlimited., build_pricing_plan_adapter()

### Community 224 - "Use / Case"
Cohesion: 0.27
Nodes (9): AnalysisRunsListServicePort, ABC, AnalysisRunsListUseCase, AnalysisRunsListCommand, AnalysisRunsListResponse, analysis_runs_list(), FastMCP, MCP tool: analysis_runs_list — List AnalysisRuns. (+1 more)

### Community 225 - "Use / Case"
Cohesion: 0.27
Nodes (9): CertsListServicePort, ABC, CertsListUseCase, CertsListCommand, CertsListResponse, certs_list(), FastMCP, MCP tool: certs_list — List all certificates. (+1 more)

### Community 226 - "Use / Case"
Cohesion: 0.22
Nodes (10): PlanSpikeProvisioningServicePort, ABC, PlanSpikeProvisioningCommand, PlanSpikeProvisioningResponse, SpikeProvisioningResult, build_spike_provisioning_adapter(), plan_spike_provisioning(), FastMCP (+2 more)

### Community 227 - "Use / Case"
Cohesion: 0.27
Nodes (9): PolicyExplainDenialServicePort, ABC, PolicyExplainDenialCommand, PolicyExplainDenialUseCase, PolicyExplainDenialResponse, policy_explain_denial(), FastMCP, MCP tool: policy_explain_denial. (+1 more)

### Community 228 - "Commands / Auth"
Cohesion: 0.13
Nodes (15): auth(), group, Manage hexawyn cloud license and authentication., db(), group, Manage the local DuckDB storage (~/.hexawyn/memory.duckdb)., app(), command (+7 more)

### Community 229 - "Gitops / Ports"
Cohesion: 0.23
Nodes (13): KubernetesNamespaceAdapter, _pod_status(), Exception, V1Deployment, V1Pod, Secondary adapter — one bulk fetch of pods/deployments/services/HPAs     for a n, _to_deployment_status(), _to_hpa_status() (+5 more)

### Community 230 - "Gitops"
Cohesion: 0.23
Nodes (11): _cpu_query(), _error_rate_query(), _memory_query(), _parse_age_to_hours(), PrometheusPodMetricsBaselineAdapter, datetime, _query_window(), Real Prometheus wiring: 3 bulk range queries (CPU, memory, error rate),     one (+3 more)

### Community 231 - "Kubernetes / Ports"
Cohesion: 0.23
Nodes (10): _is_strict_mtls(), _items(), KubernetesNetworkPolicyAdapter, Any, Exception, Secondary adapter — enumerates namespaces (with pod counts) and     NetworkPolic, _to_network_policy_raw(), _translate_error() (+2 more)

### Community 232 - "Ports"
Cohesion: 0.26
Nodes (8): MCPDiscoveryAdapter, Discovers MCP tools from the local FastMCP server instance., MCPDiscoveryPort, ABC, Discover MCP tools at startup. Result cached in memory., Driven port — discovers available MCP tools., MCPToolRegistry, MCPToolSchema

### Community 233 - "Screens / Welcome"
Cohesion: 0.16
Nodes (6): ComposeResult, Submitted, WelcomeScreen, CommandInput, Any, Key

### Community 234 - "Tools / Cluster"
Cohesion: 0.25
Nodes (9): ClusterCapacityCeilingForecastServicePort, ABC, ClusterCapacityCeilingForecastCommand, ClusterCapacityCeilingForecastResponse, build_cost_forecast_adapter(), cluster_capacity_ceiling_forecast(), FastMCP, MCP tool: cluster_capacity_ceiling_forecast — Forecast cluster capacity ceiling. (+1 more)

### Community 235 - "Network / Services"
Cohesion: 0.22
Nodes (10): ExcludedNamespace, NamespaceNetworkFinding, NetworkSegmentationReport, classify_network_status(), NetworkStatus, build_report(), _build_summary(), ExcludedNamespace (+2 more)

### Community 236 - "Probe / Services"
Cohesion: 0.35
Nodes (11): MissingProbe, ProbeAuditResult, _as_bool(), _as_int(), _classify_severity(), _find_misconfigurations(), _find_missing_probes(), _first_port() (+3 more)

### Community 237 - "Gcp"
Cohesion: 0.26
Nodes (9): _as_trace_client(), _duration_ms(), Protocol, Minimal contract for the google-cloud-trace v1 client used here., Return traces matching the request filter and time window., _trace_to_spans(), TraceClient, _TraceProto (+1 more)

### Community 238 - "Gitops / Ports"
Cohesion: 0.27
Nodes (5): KubernetesPodLogsAdapter, Secondary adapter — reads pod logs from the Kubernetes API., PodLogsPort, ABC, AnalyzePodLogsRequest

### Community 239 - "Ports / Gitops"
Cohesion: 0.26
Nodes (9): OTelCrossNamespaceTrafficAdapter, Secondary adapter — queries OTel trace data to enumerate every     observed cros, CrossNamespaceFlowDict, CrossNamespaceTrafficPort, ABC, TypedDict, Port for querying cross-namespace traffic data from OTel traces     or network f, List every observed cross-namespace service-to-service call         from OTel tr (+1 more)

### Community 240 - "Commands / Cache"
Cohesion: 0.23
Nodes (12): cache(), clear(), _get_adapter(), invalidate(), command, group, option, Manage local investigation cache (RGPD-compliant). (+4 more)

### Community 241 - "Cost / Services"
Cohesion: 0.32
Nodes (10): BillingEvent, CostForecast, ResourceCost, _as_float(), _compute_current_spend(), _compute_trend(), CostForecastEngine, _month_over_month_delta() (+2 more)

### Community 242 - "Gitops"
Cohesion: 0.29
Nodes (9): _ContainerKind, KubernetesPodSecurityAdapter, Any, Exception, Secondary adapter — enumerates every Pod's security-relevant spec     fields (po, _to_container(), _to_containers(), _to_pod_spec() (+1 more)

### Community 243 - "Ports / Logger"
Cohesion: 0.21
Nodes (7): ChatPort, ABC, Handle incoming chat message and run investigation pipeline.         Returns for, Format investigation result for the chat platform.         Free tier: basic mark, Primary port for Chat — receives investigation questions from users (Slack, Team, get_logger(), Logger

### Community 244 - "Tools / Hot"
Cohesion: 0.29
Nodes (8): HotNodeAnalysisServicePort, ABC, HotNodeAnalysisCommand, build_node_analysis_adapter(), hot_node_analysis(), FastMCP, MCP tool: hot_node_analysis., register()

### Community 245 - "Screens / Context"
Cohesion: 0.23
Nodes (3): ContextPickerScreen, KubernetesClusterContext, Pressed

### Community 246 - "Services / Event"
Cohesion: 0.30
Nodes (11): NamespaceEventsConstants, Thresholds for the namespace Warning/Error events triage use case (ECA-5)., _compute_urgency(), _finalize(), get_namespace_events(), _parse_timestamp(), datetime, Domain service — filters, flags, sorts, and paginates namespace events     (ECA- (+3 more)

### Community 247 - "Services / Log"
Cohesion: 0.20
Nodes (4): PodPrioritizationConstants, Score weights for pod prioritization in log processing., AdaptiveLogProcessor, Manages token budget for LLM-bound log processing.      Enforces a safety buffer

### Community 248 - "Mttr / Services"
Cohesion: 0.39
Nodes (9): MTTRPerSeverity, MTTRTrendReport, SlowestIncident, _as_bool(), _as_int(), _compute_trend(), MTTRTrendEngine, _rank_slowest() (+1 more)

### Community 249 - "Screens / Provider"
Cohesion: 0.24
Nodes (4): ProviderSetupScreen, Pressed, Persist LLM provider, base URL, and API key to config.yaml., save_llm_config()

### Community 250 - "Services / Cluster"
Cohesion: 0.33
Nodes (10): ClusterCapacityForecastConstants, Thresholds for cluster capacity ceiling forecasting., compute_growth_rate(), _deltas(), detect_capacity_jump(), GrowthRateResult, _has_recent_spike(), _is_outlier() (+2 more)

### Community 251 - "Gitops"
Cohesion: 0.40
Nodes (3): PrometheusClusterResourceMetricsAdapter, datetime, ClusterResourceMetricsPort backed by Prometheus (PromQL).      Owns the PromQL d

### Community 252 - "Ports / Services"
Cohesion: 0.27
Nodes (7): NetworkPolicyRaw, List every NetworkPolicy across all namespaces, with ingress/         egress rul, NetworkPolicyConstants, Well-known system namespaces excluded from the East-West network     segmentatio, build_note(), group_policies_by_namespace(), NetworkStatus

### Community 253 - "Cost"
Cohesion: 0.29
Nodes (5): CostAudit, _extract_details(), _get_float(), _get_int(), _get_str()

### Community 254 - "Slack"
Cohesion: 0.36
Nodes (4): ClientConnection, _get_active_cluster_name(), Primary adapter — Slack Socket Mode client using WebSocket.      Receives Slack, SlackSocketClient

### Community 255 - "Use / Case"
Cohesion: 0.33
Nodes (4): CorrelateErrorLatencySpikesUseCaseCommand, CorrelateErrorLatencySpikesUseCase, Correlates error spikes with latency anomalies., CorrelateErrorLatencySpikesUseCaseResponse

### Community 256 - "Use / Case"
Cohesion: 0.33
Nodes (4): DiagnoseLatencySpikeUseCaseCommand, DiagnoseLatencySpikeUseCase, Diagnoses the root cause of a latency spike., DiagnoseLatencySpikeUseCaseResponse

### Community 257 - "Use / Case"
Cohesion: 0.33
Nodes (4): GetP99LatencyUseCaseCommand, GetP99LatencyUseCase, Retrieves P99 latency metrics for a service., GetP99LatencyUseCaseResponse

### Community 258 - "Use / Case"
Cohesion: 0.33
Nodes (4): GetPodLogsUseCaseCommand, GetPodLogsUseCase, Retrieves logs for a specific pod., GetPodLogsUseCaseResponse

### Community 259 - "Tools / Prometheus"
Cohesion: 0.36
Nodes (6): PrometheusQueryCommand, PrometheusQueryUseCase, prometheus_query(), FastMCP, MCP tool: prometheus_query., register()

### Community 260 - "Commands / Cluster"
Cohesion: 0.25
Nodes (8): cluster(), argument, command, group, Switch to a different cluster context., Manage Kubernetes cluster contexts., use(), clear_l1()

### Community 261 - "Use / Case"
Cohesion: 0.39
Nodes (3): InvestigateTLSCertificateCommand, InvestigateTLSCertificateUseCase, InvestigateTLSCertificateResponse

### Community 262 - "Use / Case"
Cohesion: 0.39
Nodes (3): GetNodeStatusCommand, GetNodeStatusUseCase, GetNodeStatusResponse

### Community 263 - "Use / Case"
Cohesion: 0.39
Nodes (3): DescribePodCommand, DescribePodUseCase, DescribePodResponse

### Community 264 - "Log / Services"
Cohesion: 0.36
Nodes (7): PatternClassification, A single classified, counted log pattern with a representative sample., extract_error_patterns(), _head_tail_sample(), Build the condensed representation actually handed to the summarizer.      One l, Deterministic pattern extraction — regex/keyword classifier, no LLM.      Groups, reduce_logs_for_summarization()

### Community 266 - "Config / Telemetry"
Cohesion: 0.39
Nodes (7): is_telemetry_enabled(), Telemetry is opt-in via HEXAWYN_TELEMETRY=true., Non-blocking telemetry ping on application start., Non-blocking telemetry ping after each investigation., send_investigation_telemetry(), send_startup_telemetry(), _send_telemetry()

### Community 267 - "License / Activation"
Cohesion: 0.33
Nodes (4): BaseModel, field_validator, ActivationResponse, Activation response contract — validated when received from hexa-cloud.

### Community 268 - "Slack / Config"
Cohesion: 0.43
Nodes (6): _get_active_cluster_name(), _handle_app_mention(), handle_slack_event(), Handle incoming Slack event.      Supports:     - url_verification: respond with, get_active_context(), Get the currently active kubeconfig context.     Never raises — returns None if

### Community 269 - "Gitops"
Cohesion: 0.43
Nodes (6): _detect_level(), _parse_lines(), _parse_message(), Exception, _split_timestamp(), _translate_error()

### Community 270 - "Services / Anomaly"
Cohesion: 0.33
Nodes (4): AnomalyDetectionResult, Output of a statistical anomaly detection run., Detects anomalies using Z-score method on a univariate data series.      Z-score, ZScoreAnomalyDetector

### Community 271 - "Tools / Generate"
Cohesion: 0.48
Nodes (6): _category_from_reason(), _format_report(), generate_incident_triage_report(), FastMCP, MCP tool: generate_incident_triage_report., register()

### Community 272 - "Ports"
Cohesion: 0.40
Nodes (4): AuditRBACPermissionsServicePort, ABC, AuditRBACPermissionsCommand, AuditRBACPermissionsResponse

### Community 274 - "Tools / Snapshots"
Cohesion: 0.53
Nodes (5): FastMCP, VolumeSnapshot tools — query snapshot.storage.k8s.io CRDs., register(), snapshot_get(), snapshots_list()

### Community 275 - "Config / Region"
Cohesion: 0.50
Nodes (3): Resolve the AWS region with standard precedence.      1. AWS_REGION / AWS_DEFAUL, _region_from_context(), resolve_region()

### Community 276 - "Services / Cluster"
Cohesion: 0.50
Nodes (4): predict_saturation(), date, `(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s     s, SaturationPrediction

### Community 277 - "Services / Retrieval"
Cohesion: 0.40
Nodes (3): RetrievalGate — heuristic pre-cache classifier.  Decides whether a query needs V, Decides if a query needs VSS memory retrieval, without LLM., RetrievalGate

### Community 278 - "Config / Schedule"
Cohesion: 0.60
Nodes (4): build_registry(), _certs_list(), _global_health(), UseCaseRegistry

### Community 280 - "Semantic"
Cohesion: 0.50
Nodes (3): CheckerVerdict, str, SemanticCheckResult

### Community 281 - "Services / Network"
Cohesion: 0.50
Nodes (3): classify_risk_level(), NetworkStatus, RiskLevel

### Community 284 - "Commands / Slack"
Cohesion: 0.67
Nodes (3): group, Manage Slack integration., slack()

### Community 287 - "Logging / Tool"
Cohesion: 0.67
Nodes (3): log_tool_execution(), P, R

## Knowledge Gaps
- **39 isolated node(s):** `ClusterCertificateHealthCommand`, `ClusterCertificateHealthResponse`, `SpikeProvisioningResult`, `SeverityBreakdown`, `ImpactedService` (+34 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VanillaAdapter` connect `Vanilla` to `Gcp / Aws`, `Ports / Vanilla`, `Mock / Ports`, `Tools / Snapshots`, `Gitops / Azure`, `Azure`, `Openshift / Ports`, `Gitops / Azure`, `Memory / Duckdb`, `Namespace / Services`, `Use / Case`, `Use / Case`, `Cost / Services`, `Rightsizing / Services`, `Gitops / Certificates`, `Use / Case`, `Simulation / Services`, `Ports / Use`, `Gitops / Errors`, `Use / Case`, `Tools / Cluster`, `Use / Case`, `Zombie / Services`, `Gitops / Keda`, `Server / Config`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Why does `K8sPort` connect `Gcp / Aws` to `Use / Case`, `Vanilla`, `Ports / Vanilla`, `Use / Case`, `Use / Case`, `Use / Case`, `Mock / Ports`, `Use / Case`, `Label / Use`, `Namespace / Services`, `Use / Case`, `Log / Use`, `Use / Case`, `Use / Case`, `Datadog / Gcp`, `Azure`, `Openshift / Ports`, `Use / Case`, `Ports / Historical`, `Use / Case`, `Use / Case`, `Adaptive / Use`, `Services / Event`, `Use / Case`, `Gitops`, `Use / Case`, `Use / Case`, `Gitops / Ports`, `Server / Config`, `Use / Case`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `ClusterUnreachableError` connect `Gitops / Azure` to `Gcp / Aws`, `Vanilla`, `Ports / Vanilla`, `Secret / Services`, `Ports / Use`, `Gitops / Ports`, `External / Use`, `Log / Use`, `Gitops`, `Gitops / Ports`, `Openshift / Cluster`, `Gcp / Aws`, `Datadog / Gcp`, `Azure`, `Openshift / Machine`, `Openshift / Ports`, `Use / Case`, `Ports / Pipeline`, `Aws`, `Fleet / Config`, `Use / Case`, `Memory / Duckdb`, `Gitops / Ports`, `License / Errors`, `Services / Log`, `Datadog / Kubernetes`, `Gitops / Ports`, `Gitops / Ports`, `Kubernetes / Ports`, `Gitops / Ports`, `Gitops / Ports`, `Gitops`, `Server / Config`, `Ports / Gitops`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `VanillaAdapter` (e.g. with `AWSEKSAdapter` and `_DescribeClusterResponse`) actually correct?**
  _`VanillaAdapter` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Are the 78 inferred relationships involving `ClusterUnreachableError` (e.g. with `AWSCostAdapter` and `CostExplorerClient`) actually correct?**
  _`ClusterUnreachableError` has 78 INFERRED edges - model-reasoned connections that need verification._
- **Are the 73 inferred relationships involving `InsufficientPermissionsError` (e.g. with `AWSCostAdapter` and `CostExplorerClient`) actually correct?**
  _`InsufficientPermissionsError` has 73 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `K8sPort` (e.g. with `CloudProvider` and `AWSEKSProvider`) actually correct?**
  _`K8sPort` has 51 INFERRED edges - model-reasoned connections that need verification._