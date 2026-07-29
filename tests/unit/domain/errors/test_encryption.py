import secrets
from pathlib import Path
from unittest.mock import patch

import pytest
from hexawyn.domain.errors import EncryptionError

KUBECONFIG_SAMPLE = b"""apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTi...FAKE_CERT_DATA
    server: https://my-cluster.example.com:6443
  name: prod-eu
contexts:
- context:
    cluster: prod-eu
    namespace: default
    user: admin
  name: prod-eu
current-context: prod-eu
users:
- name: admin
  user:
    client-certificate-data: LS0tLS1CRUdJTi...FAKE_CLIENT_DATA
    client-key-data: LS0tLS1CRUdJTi...FAKE_KEY_DATA
"""

KUBECONFIG_OTHER = b"""apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: OTHER_CERT_DATA_HERE
    server: https://other-cluster.example.com:6443
  name: staging-us
"""


class TestDeriveKey:
    """Key derivation from kubeconfig content."""

    def test_same_kubeconfig_produces_same_key(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _reset_salt, derive_key

        _reset_salt()
        salt_file = tmp_path / ".keysalt"
        salt = secrets.token_bytes(32)
        salt_file.write_bytes(salt)

        with patch("hexawyn.infrastructure.memory.encryption.KEY_SALT_PATH", salt_file):
            key1 = derive_key(KUBECONFIG_SAMPLE)
            key2 = derive_key(KUBECONFIG_SAMPLE)
            assert key1 == key2

    def test_different_kubeconfig_produces_different_key(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _reset_salt, derive_key

        _reset_salt()
        salt_file = tmp_path / ".keysalt"
        salt_file.write_bytes(secrets.token_bytes(32))

        with patch("hexawyn.infrastructure.memory.encryption.KEY_SALT_PATH", salt_file):
            key1 = derive_key(KUBECONFIG_SAMPLE)
            key2 = derive_key(KUBECONFIG_OTHER)
            assert key1 != key2

    def test_key_is_32_bytes(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _reset_salt, derive_key

        _reset_salt()
        salt_file = tmp_path / ".keysalt"
        salt_file.write_bytes(secrets.token_bytes(32))

        with patch("hexawyn.infrastructure.memory.encryption.KEY_SALT_PATH", salt_file):
            key = derive_key(KUBECONFIG_SAMPLE)
            assert len(key) == 32  # noqa: PLR2004


class TestEncryptDecrypt:
    """AES-GCM encrypt/decrypt roundtrip."""

    def test_roundtrip_with_valid_key(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _decrypt_data, _encrypt_data

        key = secrets.token_bytes(32)
        plaintext = b"Du contenu confidentiel de DuckDB"

        encrypted = _encrypt_data(key, plaintext)
        assert encrypted != plaintext
        assert len(encrypted) > len(plaintext)

        decrypted = _decrypt_data(key, encrypted)
        assert decrypted == plaintext

    def test_decrypt_with_wrong_key_raises_encryption_error(self):
        from hexawyn.infrastructure.memory.encryption import _decrypt_data, _encrypt_data

        key1 = secrets.token_bytes(32)
        key2 = secrets.token_bytes(32)
        plaintext = b"Donnees chiffrees"

        encrypted = _encrypt_data(key1, plaintext)

        with pytest.raises(EncryptionError):
            _decrypt_data(key2, encrypted)

    def test_decrypt_corrupted_data_raises_encryption_error(self):
        from hexawyn.infrastructure.memory.encryption import _decrypt_data

        key = secrets.token_bytes(32)
        corrupted = b"ceci_n_est_pas_une_donnee_chiffree"

        with pytest.raises(EncryptionError):
            _decrypt_data(key, corrupted)

    def test_decrypt_too_short_data_raises_encryption_error(self):
        from hexawyn.infrastructure.memory.encryption import _decrypt_data

        key = secrets.token_bytes(32)
        too_short = b"ab"

        with pytest.raises(EncryptionError) as exc_info:
            _decrypt_data(key, too_short)
        assert "too short" in str(exc_info.value).lower()


class TestFileEncryption:
    """File-level encrypt/decrypt operations."""

    def test_encrypt_file_creates_encrypted_copy(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _encrypt_file

        key = secrets.token_bytes(32)
        plain_path = tmp_path / "test.duckdb"
        enc_path = tmp_path / "test.duckdb.enc"

        plain_path.write_bytes(b"contenu de la base de donnees")

        _encrypt_file(key, plain_path, enc_path)

        assert enc_path.exists()
        assert enc_path.read_bytes() != b"contenu de la base de donnees"

    def test_decrypt_file_restores_original(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _decrypt_file, _encrypt_file

        key = secrets.token_bytes(32)
        plain_path = tmp_path / "test.duckdb"
        enc_path = tmp_path / "test.duckdb.enc"
        output_path = tmp_path / "test_restored.duckdb"

        original = b"contenu original de DuckDB"
        plain_path.write_bytes(original)
        _encrypt_file(key, plain_path, enc_path)
        plain_path.unlink()

        _decrypt_file(key, enc_path, output_path)

        assert output_path.read_bytes() == original

    def test_encrypt_file_permissions_are_restrictive(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import _encrypt_file

        key = secrets.token_bytes(32)
        plain_path = tmp_path / "test.duckdb"
        enc_path = tmp_path / "test.duckdb.enc"

        plain_path.write_bytes(b"contenu")

        _encrypt_file(key, plain_path, enc_path)

        import stat

        file_mode = enc_path.stat().st_mode
        assert file_mode & stat.S_IROTH == 0
        assert file_mode & stat.S_IWOTH == 0


class TestPrepareDb:
    """Integration of prepare_db lifecycle."""

    def test_prepare_db_decrypts_existing_encrypted_db(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import (
            _encrypt_file,
            _reset_prepare_db_state,
            prepare_db,
        )

        key = secrets.token_bytes(32)
        plain_path = tmp_path / "memory.duckdb"
        enc_path = tmp_path / "memory.duckdb.enc"

        plain_path.write_bytes(b"donnees chiffrees au repos")

        with patch("hexawyn.infrastructure.memory.encryption.ENCRYPTED_DB_PATH", enc_path):
            with patch("hexawyn.infrastructure.memory.encryption.DB_PATH", plain_path):
                with patch("hexawyn.infrastructure.memory.encryption.HEXAWYN_DIR", tmp_path):
                    _encrypt_file(key, plain_path, enc_path)
                    plain_path.unlink()

                    _reset_prepare_db_state()
                    prepare_db(key)

                    assert plain_path.exists()
                    assert plain_path.read_bytes() == b"donnees chiffrees au repos"

    def test_prepare_db_handles_fresh_start_no_files(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import (
            _reset_prepare_db_state,
            prepare_db,
        )

        key = secrets.token_bytes(32)
        plain_path = tmp_path / "memory.duckdb"
        enc_path = tmp_path / "memory.duckdb.enc"

        assert not plain_path.exists()
        assert not enc_path.exists()

        with patch("hexawyn.infrastructure.memory.encryption.ENCRYPTED_DB_PATH", enc_path):
            with patch("hexawyn.infrastructure.memory.encryption.DB_PATH", plain_path):
                with patch("hexawyn.infrastructure.memory.encryption.HEXAWYN_DIR", tmp_path):
                    _reset_prepare_db_state()
                    prepare_db(key)

                    assert not plain_path.exists()
                    assert not enc_path.exists()


class TestEncryptionDisabled:
    """Encryption can be disabled via env var."""

    def test_is_encryption_disabled_returns_true_when_env_set(self):
        from hexawyn.infrastructure.memory.encryption import is_encryption_disabled

        with patch.dict("os.environ", {"HEXAWYN_DISABLE_ENCRYPTION": "true"}):
            assert is_encryption_disabled() is True

    def test_is_encryption_disabled_returns_false_when_env_not_set(self):
        from hexawyn.infrastructure.memory.encryption import is_encryption_disabled

        with patch.dict("os.environ", {}, clear=True):
            assert is_encryption_disabled() is False

    def test_is_encryption_disabled_returns_false_for_false_value(self):
        from hexawyn.infrastructure.memory.encryption import is_encryption_disabled

        with patch.dict("os.environ", {"HEXAWYN_DISABLE_ENCRYPTION": "false"}):
            assert is_encryption_disabled() is False


class TestGetOrCreateSalt:
    """Salt creation and caching behavior."""

    def test_creates_new_salt_when_file_missing(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.memory.encryption import _get_or_create_salt, _reset_salt

        _reset_salt()
        salt_path = tmp_path / ".keysalt"
        with patch("hexawyn.infrastructure.memory.encryption.KEY_SALT_PATH", salt_path):
            salt = _get_or_create_salt()
            assert len(salt) == 32  # noqa: PLR2004
            assert salt_path.exists()

    def test_caches_salt_after_first_call(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.memory.encryption import _get_or_create_salt, _reset_salt

        _reset_salt()
        salt_path = tmp_path / ".keysalt"
        salt_path.write_bytes(secrets.token_bytes(32))
        with patch("hexawyn.infrastructure.memory.encryption.KEY_SALT_PATH", salt_path):
            salt1 = _get_or_create_salt()
            salt2 = _get_or_create_salt()
            assert salt1 == salt2


class TestEncryptFileEdges:
    """Edge cases for _encrypt_file and _decrypt_file."""

    def test_encrypt_file_noop_when_plain_missing(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.memory.encryption import _encrypt_file

        key = secrets.token_bytes(32)
        plain_path = tmp_path / "nonexistent.duckdb"
        enc_path = tmp_path / "nonexistent.duckdb.enc"

        _encrypt_file(key, plain_path, enc_path)
        assert not enc_path.exists()

    def test_decrypt_file_noop_when_enc_missing(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.memory.encryption import _decrypt_file

        key = secrets.token_bytes(32)
        enc_path = tmp_path / "nonexistent.duckdb.enc"
        output_path = tmp_path / "nonexistent.duckdb"

        _decrypt_file(key, enc_path, output_path)
        assert not output_path.exists()


class TestEncryptDbOnExit:
    """Cover _encrypt_db_on_exit function."""

    def test_encrypts_and_removes_db_on_exit(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.memory.encryption import _encrypt_db_on_exit

        key = secrets.token_bytes(32)
        db_path = tmp_path / "memory.duckdb"
        enc_path = tmp_path / "memory.duckdb.enc"

        db_path.write_bytes(b"database content for on-exit test")

        with patch("hexawyn.infrastructure.memory.encryption.DB_PATH", db_path):
            with patch("hexawyn.infrastructure.memory.encryption.ENCRYPTED_DB_PATH", enc_path):
                _encrypt_db_on_exit(key)

        assert enc_path.exists()
        assert enc_path.read_bytes() != b"database content for on-exit test"
        assert not db_path.exists()

    def test_encrypt_db_on_exit_noop_when_db_missing(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.memory.encryption import _encrypt_db_on_exit

        key = secrets.token_bytes(32)
        db_path = tmp_path / "nonexistent.duckdb"
        enc_path = tmp_path / "nonexistent.duckdb.enc"

        with patch("hexawyn.infrastructure.memory.encryption.DB_PATH", db_path):
            with patch("hexawyn.infrastructure.memory.encryption.ENCRYPTED_DB_PATH", enc_path):
                _encrypt_db_on_exit(key)

        assert not enc_path.exists()


class TestResetState:
    """Reset state functions for test isolation."""

    def test_reset_prepare_db_state_clears_flags(self) -> None:
        import hexawyn.infrastructure.memory.encryption as enc_mod

        enc_mod._reset_prepare_db_state()
        assert enc_mod._db_prepared is False
        assert enc_mod._atexit_registered is False

    def test_reset_salt_clears_cache(self) -> None:
        import hexawyn.infrastructure.memory.encryption as enc_mod

        enc_mod._salt_cache = b"fake-salt"
        enc_mod._reset_salt()
        assert enc_mod._salt_cache is None

    def test_prepare_db_idempotent_second_call_noop(self, tmp_path: Path) -> None:
        import hexawyn.infrastructure.memory.encryption as enc_mod

        enc_mod._reset_prepare_db_state()
        key = secrets.token_bytes(32)
        plain_path = tmp_path / "memory.duckdb"
        enc_path = tmp_path / "memory.duckdb.enc"

        with patch("hexawyn.infrastructure.memory.encryption.ENCRYPTED_DB_PATH", enc_path):
            with patch("hexawyn.infrastructure.memory.encryption.DB_PATH", plain_path):
                with patch("hexawyn.infrastructure.memory.encryption.HEXAWYN_DIR", tmp_path):
                    enc_mod.prepare_db(key)
                    assert enc_mod._db_prepared is True
                    enc_mod.prepare_db(key)
                    assert enc_mod._db_prepared is True


class TestKubeconfigKeyDerivation:
    """Integration: derives key from stable kubeconfig parts."""

    def test_extract_stable_parts_from_kubeconfig(self, tmp_path: Path):
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        kubeconfig_file = tmp_path / "config"
        kubeconfig_file.write_text(
            """apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: ZmFrZS1jYS1jZXJ0
    server: https://prod-eu.example.com:6443
  name: prod-eu
"""
        )

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            content = get_kubeconfig_stable_content()

        assert content is not None
        assert b"prod-eu.example.com" in content
        assert b"ZmFrZS1jYS1jZXJ0" in content

    def test_extract_stable_parts_multiple_clusters(self, tmp_path: Path):
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        kubeconfig_file = tmp_path / "config"
        kubeconfig_file.write_text(
            """apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: Y2EtMQ==
    server: https://cluster1.example.com:6443
  name: cluster1
- cluster:
    certificate-authority-data: Y2EtMg==
    server: https://cluster2.example.com:6443
  name: cluster2
"""
        )

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            content = get_kubeconfig_stable_content()

        assert content is not None
        assert b"cluster1.example.com" in content
        assert b"Y2EtMQ==" in content
        assert b"cluster2.example.com" in content
        assert b"Y2EtMg==" in content

    def test_extract_stable_parts_no_kubeconfig_returns_none(self):
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        with patch.dict("os.environ", {}, clear=True):
            with patch("os.path.exists", return_value=False):
                content = get_kubeconfig_stable_content()
                assert content is None

    def test_non_dict_config_returns_raw_bytes(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        kubeconfig_file = tmp_path / "config"
        kubeconfig_file.write_text("- just a list\n- not a dict\n")

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            content = get_kubeconfig_stable_content()

        assert content is not None
        assert b"just a list" in content

    def test_clusters_not_a_list_returns_raw_bytes(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        kubeconfig_file = tmp_path / "config"
        kubeconfig_file.write_text("apiVersion: v1\nclusters: not_a_list\n")

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            content = get_kubeconfig_stable_content()

        assert content is not None

    def test_empty_stable_parts_returns_raw_bytes(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        kubeconfig_file = tmp_path / "config"
        kubeconfig_file.write_text("apiVersion: v1\nclusters:\n- name: empty\n  cluster: {}\n")

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            content = get_kubeconfig_stable_content()

        assert content is not None

    def test_yaml_parse_error_returns_none(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.config.kubeconfig_reader import (
            get_kubeconfig_stable_content,
        )

        kubeconfig_file = tmp_path / "config"
        kubeconfig_file.write_text(": invalid: yaml: : :\n")

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            content = get_kubeconfig_stable_content()

        assert content is None


class TestEndToEndEncryptDecrypt:
    """Full end-to-end: derive key from kubeconfig → encrypt → decrypt."""

    def test_e2e_encrypt_decrypt_with_kubeconfig_content(self, tmp_path: Path):
        from hexawyn.infrastructure.memory.encryption import (
            _decrypt_data,
            _encrypt_data,
            _reset_salt,
            derive_key,
        )

        _reset_salt()
        salt_file = tmp_path / ".keysalt"
        salt_file.write_bytes(secrets.token_bytes(32))

        kubeconfig_content = b"fake-kubeconfig-content-for-cluster-xyz"

        with patch("hexawyn.infrastructure.memory.encryption.KEY_SALT_PATH", salt_file):
            key = derive_key(kubeconfig_content)

        original = b"donnees sensibles de la base DuckDB"
        encrypted = _encrypt_data(key, original)
        decrypted = _decrypt_data(key, encrypted)

        assert decrypted == original
        assert encrypted != original
