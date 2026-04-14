from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.auth import (  # noqa: E402
    init_tokens_file,
    load_bearer_auth_config,
    load_tokens_file,
    revoke_token,
    rotate_token,
    upsert_token,
)


class LingxingTokenAuthTests(unittest.TestCase):
    def test_single_token_mode_stays_compatible_without_tokens_file(self) -> None:
        config = load_bearer_auth_config(
            bootstrap_token="bootstrap-token",
            tokens_file=str(Path(tempfile.gettempdir()) / "missing-lingxing-token-file.json"),
        )
        self.assertTrue(config.has_any())
        self.assertEqual(config.auth_modes(), ["single"])
        match = config.authenticate_header("Bearer bootstrap-token")
        self.assertIsNotNone(match)
        self.assertEqual(match.token_id, "bootstrap")

    def test_token_lifecycle_init_add_rotate_revoke(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            tokens_file = Path(temp_dir) / "tokens.json"
            _, admin_token = init_tokens_file(tokens_file, token_id="admin", description="Admin token")
            records = load_tokens_file(tokens_file)
            self.assertEqual(records[0].token_id, "admin")
            self.assertEqual(records[0].token, admin_token)

            member_token = upsert_token(tokens_file, token_id="alice-mac", description="Alice MacBook")
            config = load_bearer_auth_config(tokens_file=str(tokens_file))
            match = config.authenticate_header(f"Bearer {member_token}")
            self.assertIsNotNone(match)
            self.assertEqual(match.token_id, "alice-mac")

            rotated = rotate_token(tokens_file, token_id="alice-mac")
            refreshed = load_bearer_auth_config(tokens_file=str(tokens_file))
            self.assertIsNone(refreshed.authenticate_header(f"Bearer {member_token}"))
            refreshed_match = refreshed.authenticate_header(f"Bearer {rotated}")
            self.assertIsNotNone(refreshed_match)
            self.assertEqual(refreshed_match.token_id, "alice-mac")

            changed = revoke_token(tokens_file, token_id="alice-mac")
            revoked = load_bearer_auth_config(tokens_file=str(tokens_file))
            self.assertTrue(changed)
            self.assertIsNone(revoked.authenticate_header(f"Bearer {rotated}"))

    def test_tokens_file_supports_active_member_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            tokens_file = Path(temp_dir) / "tokens.json"
            tokens_file.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "tokens": [
                            {"id": "alice", "description": "Alice", "token": "alice-token", "status": "active"},
                            {"id": "bob", "description": "Bob", "token": "bob-token", "status": "revoked"},
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            config = load_bearer_auth_config(tokens_file=str(tokens_file))
            self.assertEqual(config.summary()["active_member_tokens"], 1)
            match = config.authenticate_header("Bearer alice-token")
            self.assertIsNotNone(match)
            self.assertEqual(match.token_id, "alice")
            self.assertIsNone(config.authenticate_header("Bearer bob-token"))


if __name__ == "__main__":
    unittest.main()
