from hexawyn.adapters.secondary.gcp.gke_context_parser import parse_gke_context


class TestParseGKEContext:
    def test_parses_project_region_cluster(self) -> None:
        result = parse_gke_context("gke_my-project_europe-west1_prod-cluster")

        assert result == {
            "project_id": "my-project",
            "region": "europe-west1",
            "cluster": "prod-cluster",
        }

    def test_returns_none_without_gke_prefix(self) -> None:
        assert parse_gke_context("minikube") is None

    def test_returns_none_when_parts_missing(self) -> None:
        assert parse_gke_context("gke_my-project_europe-west1") is None

    def test_returns_none_when_extra_parts(self) -> None:
        assert parse_gke_context("gke_p_r_c_extra") is None

    def test_returns_none_when_a_part_is_empty(self) -> None:
        assert parse_gke_context("gke_my-project__prod") is None
