from __future__ import annotations

from unittest.mock import MagicMock


class TestDetectNetworkSegmentationGapsUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.command import (  # noqa: E501
            DetectNetworkSegmentationGapsCommand,
        )
        from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.detect_network_segmentation_gaps_use_case import (  # noqa: E501
            DetectNetworkSegmentationGapsUseCase,
        )
        from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.response import (  # noqa: E501
            DetectNetworkSegmentationGapsResponse,
        )

        port = MagicMock()
        port.list_namespaces_with_pod_counts.return_value = []
        port.list_network_policies.return_value = []
        port.has_calico_global_network_policies.return_value = False
        port.has_istio_strict_peer_authentication.return_value = False

        use_case = DetectNetworkSegmentationGapsUseCase(port=port)
        result = use_case.execute(DetectNetworkSegmentationGapsCommand())

        assert isinstance(result, DetectNetworkSegmentationGapsResponse)


class TestGetPipelineRunStatusUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
            GetPipelineRunStatusCommand,
        )
        from hexawyn.application.use_case.pipelines.get_pipeline_run_status.get_pipeline_run_status_use_case import (  # noqa: E501
            GetPipelineRunStatusUseCase,
        )
        from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
            GetPipelineRunStatusResponse,
        )

        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = GetPipelineRunStatusUseCase(port=port)
        result = use_case.execute(GetPipelineRunStatusCommand())

        assert isinstance(result, GetPipelineRunStatusResponse)


class TestDetectUnintendedExternalExposureUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.networking.detect_unintended_external_exposure.command import (  # noqa: E501
            DetectUnintendedExternalExposureCommand,
        )
        from hexawyn.application.use_case.networking.detect_unintended_external_exposure.detect_unintended_external_exposure_use_case import (  # noqa: E501
            DetectUnintendedExternalExposureUseCase,
        )
        from hexawyn.application.use_case.networking.detect_unintended_external_exposure.response import (  # noqa: E501
            DetectUnintendedExternalExposureResponse,
        )

        port = MagicMock()
        port.list_external_services.return_value = []

        use_case = DetectUnintendedExternalExposureUseCase(port=port)
        result = use_case.execute(DetectUnintendedExternalExposureCommand())

        assert isinstance(result, DetectUnintendedExternalExposureResponse)


class TestCheckResourceConstraintsUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.cluster.check_resource_constraints.check_resource_constraints_use_case import (  # noqa: E501
            CheckResourceConstraintsUseCase,
        )
        from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
            CheckResourceConstraintsCommand,
        )
        from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
            CheckResourceConstraintsResponse,
        )

        port = MagicMock()
        port.list_container_resources.return_value = []

        use_case = CheckResourceConstraintsUseCase(port=port)
        result = use_case.execute(CheckResourceConstraintsCommand())

        assert isinstance(result, CheckResourceConstraintsResponse)
