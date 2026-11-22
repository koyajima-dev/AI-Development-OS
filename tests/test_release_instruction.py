import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from release_instruction import release
from test_instruction_gate import GOOD
class TestRelease(unittest.TestCase):
 def test_valid(self):
  s=GOOD.replace("公式確認：未確認","公式確認：確認済み").replace("環境選択可否：未確認","環境選択可否：確認済み")
  self.assertEqual(release(s),[])
 def test_official_unknown(self):
  self.assertIn("official_unconfirmed",release(GOOD))
 def test_environment_unknown(self):
  self.assertIn("environment_unconfirmed",release(GOOD))
 def test_missing_model(self):
  self.assertIn("specific_model",release(GOOD.replace("推奨モデル：Claude Sonnet 4.5","")))
if __name__=="__main__":unittest.main()
