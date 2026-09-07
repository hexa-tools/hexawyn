from unittest.mock import MagicMock, patch


class TestRefreshLicense:
    def test_refresh_writes_new_jwt(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        mock_client = MagicMock()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "token": "new.jwt.token",
            "plan": "team",
            "expires_at": "2026-09-01T00:00:00Z",
        }
        mock_client.__enter__.return_value.post.return_value = mock_resp

        mock_client_class = MagicMock(return_value=mock_client)

        with (
            patch("hexawyn.infrastructure.license.license_reader.httpx.Client", mock_client_class),
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "test_key"},
            ),
            patch("hexawyn.infrastructure.config.machine_id.get_machine_id", return_value="m1"),
            patch("pathlib.Path.mkdir"),
            patch("pathlib.Path.write_text") as mock_write,
        ):
            result = refresh_license()

        assert result is True
        mock_write.assert_called_once_with("new.jwt.token")

    def test_refresh_returns_false_when_no_token(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        with patch("hexawyn.infrastructure.config.config_manager.load_config", return_value={}):
            result = refresh_license()

        assert result is False

    def test_refresh_returns_false_on_error(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        with patch("hexawyn.infrastructure.config.config_manager.load_config", side_effect=OSError):
            result = refresh_license()

        assert result is False
