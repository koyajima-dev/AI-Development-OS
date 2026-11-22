#!/usr/bin/env python3
"""Fail-closed structural gate for AI implementation instructions. Not a factual verifier."""
import pathlib, re, sys

HEADINGS = {
 "purpose": r"目的|Target", "evidence": r"現在地|Evidence|確認済み",
 "preflight": r"Preflight|実行前", "reuse": r"再利用|既存資産",
 "past_failures": r"FAIL|BLOCKED|失敗履歴", "fallback": r"代替経路|引き継ぎ",
 "scope": r"変更範囲|禁止事項", "cost": r"総作業量|総コスト",
 "model": r"モデル選定|モデルと推論", "acceptance": r"Acceptance|合格条件",
 "verification": r"検証", "stop": r"停止条件", "evidence_save": r"Evidence保存|証跡保存",
 "human": r"Human判断|Human Decision|承認条件"
}
FIELDS = {
 "specific_model": r"推奨モデル\s*[:：]\s*\S+",
 "effort": r"(?:推論レベル|Effort)\s*[:：]\s*(?:Low|Medium|High|Extra High|低|中|高)",
 "reason": r"選定理由\s*[:：]\s*\S+",
 "escalation": r"(?:上位切替条件|切替条件)\s*[:：]\s*\S+",
 "human_stop": r"Human停止点\s*[:：]\s*\S+",
 "official": r"公式確認\s*[:：]\s*(?:確認済み|未確認)",
 "availability": r"環境選択可否\s*[:：]\s*(?:確認済み|未確認)",
 "unavailable": r"利用不可時\s*[:：].*停止"
}
def validate(s):
    missing = [k for k,p in HEADINGS.items() if not re.search(r"(?im)^#{1,4}\s*.*(?:"+p+")",s)]
    missing += [k for k,p in FIELDS.items() if not re.search(p,s,re.I)]
    if re.search(r"前の指示書に追記|末尾に追加|差分指示",s): missing.append("full_document_only")
    return missing

if __name__ == "__main__":
    if len(sys.argv)!=2: sys.exit("usage: python3 scripts/instruction_gate.py draft.md")
    path=pathlib.Path(sys.argv[1])
    try: content=path.read_text(encoding="utf-8")
    except (OSError,UnicodeError) as e: sys.exit(f"BLOCKED: {e}")
    missing=validate(content)
    if missing:
        print("FAIL: "+", ".join(missing));sys.exit(1)
    print("PASS: structural only; verify model facts and environment independently")
