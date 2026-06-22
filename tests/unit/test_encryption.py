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
            assert len(key) == 32


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
