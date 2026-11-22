import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from instruction_gate import validate

GOOD = """# 目的
# 現在地 Evidence
# Preflight
# 既存資産再利用
# 過去のFAIL
# 代替経路
# 禁止事項
# 総作業量
# モデル選定
推奨モデル：Claude Sonnet 4.5
推論レベル：High
選定理由：実機照合が必要
上位切替条件：設計矛盾
Human停止点：設計変更前
公式確認：未確認
環境選択可否：未確認
利用不可時：停止して報告
# Acceptance
# 検証
# 停止条件
# Evidence保存
# Human判断
"""
class TestGate(unittest.TestCase):
 def test_valid(self): self.assertEqual(validate(GOOD),[])
 def test_empty(self): self.assertTrue(validate(""))
 def test_model_missing(self): self.assertIn("specific_model",validate(GOOD.replace("推奨モデル：Claude Sonnet 4.5","")))
 def test_effort_missing(self): self.assertIn("effort",validate(GOOD.replace("推論レベル：High","")))
 def test_reason_missing(self): self.assertIn("reason",validate(GOOD.replace("選定理由：実機照合が必要","")))
 def test_human_stop_missing(self): self.assertIn("human_stop",validate(GOOD.replace("Human停止点：設計変更前","")))
 def test_patch_rejected(self): self.assertIn("full_document_only",validate(GOOD+"\n末尾に追加"))
 def test_model_availability_missing(self): self.assertIn("availability",validate(GOOD.replace("環境選択可否：未確認","")))
 def test_model_official_missing(self): self.assertIn("official",validate(GOOD.replace("公式確認：未確認","")))
 def test_no_semantic_guarantee(self): self.assertEqual(validate(GOOD.replace("Claude Sonnet 4.5","架空モデルX")),[])
if __name__=="__main__": unittest.main()
