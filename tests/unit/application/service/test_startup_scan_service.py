class TestStartupScanService:
    def test_valid_result_with_pods_and_score(self) -> None:
        from hexawyn.application.service.startup_scan_service import (
            is_valid_startup_result,
        )

        result = {
            "health_score": 85,
            "narrative_summary": "Cluster looks good",
            "cluster_summary": {"total_pods": 10},
        }
        assert is_valid_startup_result(result) is True

    def test_invalid_zero_health_score(self) -> None:
        from hexawyn.application.service.startup_scan_service import (
            is_valid_startup_result,
        )

        result = {
            "health_score": 0,
            "narrative_summary": "ok",
            "cluster_summary": {"total_pods": 10},
        }
        assert is_valid_startup_result(result) is False

    def test_invalid_no_pods(self) -> None:
        from hexawyn.application.service.startup_scan_service import (
            is_valid_startup_result,
        )

        result = {
            "health_score": 85,
            "narrative_summary": "ok",
            "cluster_summary": {"total_pods": 0},
        }
        assert is_valid_startup_result(result) is False

    def test_invalid_error_narrative(self) -> None:
        from hexawyn.application.service.startup_scan_service import (
            is_valid_startup_result,
        )

        result = {
            "health_score": 85,
            "narrative_summary": "Runtime not available",
            "cluster_summary": {"total_pods": 10},
        }
        assert is_valid_startup_result(result) is False

    def test_valid_minimal(self) -> None:
        from hexawyn.application.service.startup_scan_service import (
            is_valid_startup_result,
        )

        result = {
            "health_score": 50,
            "narrative_summary": "All good",
            "cluster_summary": {"total_pods": 1},
        }
        assert is_valid_startup_result(result) is True

    def test_is_error_narrative_filters_known_issues(self) -> None:
        from hexawyn.application.service.startup_scan_service import (
            is_error_narrative,
        )

        assert is_error_narrative("Runtime not available. Check config.") is True
        assert is_error_narrative("Cluster looks healthy") is False
        assert is_error_narrative("No pods found in namespace") is True
        assert is_error_narrative("All systems operational") is False
