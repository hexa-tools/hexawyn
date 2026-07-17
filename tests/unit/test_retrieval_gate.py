"""Tests for RetrievalGate — heuristic pre-cache classifier."""

from hexawyn.domain.services.retrieval_gate import RetrievalGate


class TestRetrievalGateSkip:
    """Queries that should NOT trigger memory retrieval."""

    def _gate(self) -> RetrievalGate:
        return RetrievalGate()

    def test_list_namespaces(self) -> None:
        assert self._gate().should_retrieve("list namespaces") is False

    def test_show_me_pods(self) -> None:
        assert self._gate().should_retrieve("show me pods in payments") is False

    def test_count_deployments(self) -> None:
        assert self._gate().should_retrieve("count deployments in prod") is False

    def test_what_is_version(self) -> None:
        assert self._gate().should_retrieve("what is the version of nginx") is False

    def test_how_many_nodes(self) -> None:
        assert self._gate().should_retrieve("how many nodes") is False

    def test_get_pod_status(self) -> None:
        assert self._gate().should_retrieve("get pod status for payments-api") is False

    def test_list_pods(self) -> None:
        assert self._gate().should_retrieve("list pods") is False

    def test_empty_query(self) -> None:
        assert self._gate().should_retrieve("") is False

    def test_short_simple_query(self) -> None:
        assert self._gate().should_retrieve("pods") is False


class TestRetrievalGateRetrieve:
    """Queries that SHOULD trigger memory retrieval."""

    def _gate(self) -> RetrievalGate:
        return RetrievalGate()

    def test_why_crashing(self) -> None:
        assert self._gate().should_retrieve("why is payments-api crashing") is True

    def test_debug_oom(self) -> None:
        assert self._gate().should_retrieve("debug the OOM in auth-service") is True

    def test_whats_wrong(self) -> None:
        assert self._gate().should_retrieve("what's wrong with payments-api") is True

    def test_investigate_crashloop(self) -> None:
        assert self._gate().should_retrieve("investigate crashloop in prod") is True

    def test_root_cause(self) -> None:
        assert self._gate().should_retrieve("root cause of high restart count") is True

    def test_oomkilled_history(self) -> None:
        assert self._gate().should_retrieve("OOMKilled payments-api last week") is True

    def test_single_oom(self) -> None:
        assert self._gate().should_retrieve("OOM") is True

    def test_single_why(self) -> None:
        assert self._gate().should_retrieve("why") is True

    def test_fix_pod(self) -> None:
        assert self._gate().should_retrieve("fix the payments-api pod") is True

    def test_troubleshoot(self) -> None:
        assert self._gate().should_retrieve("troubleshoot high latency") is True

    def test_error_keyword(self) -> None:
        assert self._gate().should_retrieve("ERROR payments-api") is True

    def test_diagnose(self) -> None:
        assert self._gate().should_retrieve("diagnose node pressure") is True


class TestRetrievalGateEdgeCases:
    def _gate(self) -> RetrievalGate:
        return RetrievalGate()

    def test_needs_wins_over_skip(self) -> None:
        assert self._gate().should_retrieve("show me the root cause of the crash") is True

    def test_empty_string(self) -> None:
        assert self._gate().should_retrieve("") is False

    def test_whitespace_only(self) -> None:
        assert self._gate().should_retrieve("   ") is False

    def test_tool_name_in_query(self) -> None:
        assert self._gate().should_retrieve("use crashloop_detector on payments") is True

    def test_imagepull_error(self) -> None:
        assert self._gate().should_retrieve("ImagePull payments-api") is True

    def test_pending_pod(self) -> None:
        assert self._gate().should_retrieve("pending pod in prod") is True

    def test_short_query_no_keywords(self) -> None:
        assert (
            self._gate().should_retrieve(
                "can you please tell me the current status of all the things"
            )
            is False
        )

    def test_very_long_query(self) -> None:
        query = "why is my pod crashing " * 100
        assert self._gate().should_retrieve(query) is True

    def test_memory_present_still_classifies(self) -> None:
        assert self._gate().should_retrieve("why is my deployment broken") is True

    def test_extremely_long_query_truncation(self) -> None:
        query = "please tell me about the status of things " * 100
        assert self._gate().should_retrieve(query) is False

    def test_french_query_defaults_to_needs_memory(self) -> None:
        assert self._gate().should_retrieve("pourquoi payments-api crash ?") is True

    def test_evicted_pod(self) -> None:
        assert self._gate().should_retrieve("pod evicted from node-3") is True

    def test_notready_node(self) -> None:
        assert self._gate().should_retrieve("node notready in prod-eu") is True

    def test_crashloop_keyword(self) -> None:
        assert self._gate().should_retrieve("CrashLoopBackOff on payments") is True

    def test_history_trend(self) -> None:
        assert self._gate().should_retrieve("memory trend last week") is True

    def test_yesterday_crash(self) -> None:
        assert self._gate().should_retrieve("what crashed yesterday") is True


class TestRetrievalGatePerformance:
    def test_classification_under_1ms(self) -> None:
        import time

        gate = RetrievalGate()
        queries = [
            "list namespaces",
            "why is payments-api crashing",
            "show me pods",
            "debug the OOM",
            "count deployments",
            "what's wrong with auth",
            "get pod status",
            "investigate crashloop",
            "how many nodes",
            "fix the memory leak",
        ]

        start = time.perf_counter()
        for q in queries * 10:
            gate.should_retrieve(q)
        elapsed = time.perf_counter() - start

        assert elapsed < 0.1, f"100 classifications took {elapsed:.4f}s, expected < 0.1s"
