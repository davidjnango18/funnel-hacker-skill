from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_knowledge_base import table_rows, validate  # noqa: E402


class KnowledgeBaseTests(unittest.TestCase):
    def test_manifest_has_unique_source_ids(self) -> None:
        rows = table_rows((ROOT / "references" / "SOURCE_MANIFEST.md").read_text(encoding="utf-8"))
        source_ids = [row["source_id"] for row in rows]
        self.assertEqual(len(source_ids), len(set(source_ids)))
        self.assertEqual(len(source_ids), 12)

    def test_final_knowledge_base_is_valid(self) -> None:
        self.assertEqual(validate(pre_cleanup=False), [])


if __name__ == "__main__":
    unittest.main()
