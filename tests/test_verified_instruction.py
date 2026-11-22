import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
from verified_instruction import publish


class VerifiedInstructionTests(unittest.TestCase):
    def test_rejects_missing_gate(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            source, output = root / "draft.md", root / "release.md"
            source.write_text("draft", encoding="utf-8")
            self.assertNotEqual(publish(source, output, root), 0)
            self.assertFalse(output.exists())

    def test_rejects_existing_destination(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            source, output = root / "draft.md", root / "release.md"
            source.write_text("draft", encoding="utf-8")
            output.write_text("original", encoding="utf-8")
            self.assertNotEqual(publish(source, output, root), 0)
            self.assertEqual(output.read_text(encoding="utf-8"), "original")

    def test_rejects_same_path(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            source = root / "draft.md"
            source.write_text("original", encoding="utf-8")
            self.assertNotEqual(publish(source, source, root), 0)
            self.assertEqual(source.read_text(encoding="utf-8"), "original")

    def test_gate_failure_does_not_publish(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root / "scripts").mkdir()
            (root / "scripts" / "release_instruction.py").write_text("import sys;sys.exit(1)")
            source, output = root / "draft.md", root / "release.md"
            source.write_text("incomplete", encoding="utf-8")
            self.assertNotEqual(publish(source, output, root), 0)
            self.assertFalse(output.exists())

    def test_gate_success_publishes_exact_output(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root / "scripts").mkdir()
            (root / "scripts" / "release_instruction.py").write_text('print("verified")')
            source, output = root / "draft.md", root / "release.md"
            source.write_text("draft", encoding="utf-8")
            self.assertEqual(publish(source, output, root), 0)
            self.assertEqual(output.read_bytes(), b"verified\n")


if __name__ == "__main__":
    unittest.main()
