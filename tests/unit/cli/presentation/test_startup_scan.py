class TestStartupScan:
    def test_valid_result_with_pods_and_score(self) -> None:
        from hexawyn.cli.presentation.startup_scan import is_valid_startup_result

        result = {
            "health_score": 85,
            "narrative_summary": "Cluster looks good",
            "cluster_summary": {"total_pods": 10},
        }
        assert is_valid_startup_result(result) is True

    def test_invalid_zero_health_score(self) -> None:
        from hexawyn.cli.presentation.startup_scan import is_valid_startup_result

        result = {
            "health_score": 0,
            "narrative_summary": "ok",
            "cluster_summary": {"total_pods": 10},
        }
        assert is_valid_startup_result(result) is False

    def test_invalid_no_pods(self) -> None:
        from hexawyn.cli.presentation.startup_scan import is_valid_startup_result

        result = {
            "health_score": 85,
            "narrative_summary": "ok",
            "cluster_summary": {"total_pods": 0},
        }
        assert is_valid_startup_result(result) is False

    def test_invalid_error_narrative(self) -> None:
        from hexawyn.cli.presentation.startup_scan import is_valid_startup_result

        result = {
            "health_score": 85,
            "narrative_summary": "Runtime not available",
            "cluster_summary": {"total_pods": 10},
        }
        assert is_valid_startup_result(result) is False

    def test_valid_minimal(self) -> None:
        from hexawyn.cli.presentation.startup_scan import is_valid_startup_result

        result = {
            "health_score": 50,
            "narrative_summary": "All good",
            "cluster_summary": {"total_pods": 1},
        }
        assert is_valid_startup_result(result) is True
