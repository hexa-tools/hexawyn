from abc import ABC


class TestOpenShiftResourcePortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.openshift_resource_port import (
            OpenShiftResourcePort,
        )

        assert issubclass(OpenShiftResourcePort, ABC)

    def test_declares_required_abstract_methods(self) -> None:
        from hexawyn.application.ports.driven.openshift_resource_port import (
            OpenShiftResourcePort,
        )

        expected = {
            "list_projects",
            "list_routes",
            "list_security_context_constraints",
            "list_image_streams",
        }

        assert expected <= OpenShiftResourcePort.__abstractmethods__


class TestOpenShiftResourceTypedDicts:
    def test_project_info_shape(self) -> None:
        from hexawyn.application.ports.driven.openshift_resource_port import ProjectInfo

        project: ProjectInfo = {
            "name": "team-a",
            "status": "Active",
            "display_name": "Team A",
        }

        assert project["name"] == "team-a"
        assert project["status"] == "Active"
        assert project["display_name"] == "Team A"

    def test_route_info_shape(self) -> None:
        from hexawyn.application.ports.driven.openshift_resource_port import RouteInfo

        route: RouteInfo = {
            "name": "web",
            "namespace": "team-a",
            "host": "web.apps.ocp.example.com",
            "target_service": "web-svc",
            "tls_enabled": True,
        }

        assert route["host"].endswith("example.com")
        assert route["tls_enabled"] is True

    def test_scc_info_shape(self) -> None:
        from hexawyn.application.ports.driven.openshift_resource_port import (
            SecurityContextConstraintInfo,
        )

        scc: SecurityContextConstraintInfo = {
            "name": "anyuid",
            "allow_privileged_container": False,
            "run_as_user_type": "RunAsAny",
        }

        assert scc["name"] == "anyuid"
        assert scc["allow_privileged_container"] is False

    def test_image_stream_info_shape(self) -> None:
        from hexawyn.application.ports.driven.openshift_resource_port import (
            ImageStreamInfo,
        )

        stream: ImageStreamInfo = {
            "name": "python",
            "namespace": "openshift",
            "tag_count": 4,
        }

        assert stream["tag_count"] == 4
