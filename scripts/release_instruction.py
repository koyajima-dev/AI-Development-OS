#!/usr/bin/env python3
"""Print complete instruction only when mandatory fields and confirmation statuses pass."""
import pathlib, re, sys
from instruction_gate import validate

def release(s):
    missing=validate(s)
    for label,pat in {
        "official_unconfirmed":r"(?im)^\s*(?:[-*]\s*)?公式確認\s*[:：]\s*未確認",
        "environment_unconfirmed":r"(?im)^\s*(?:[-*]\s*)?環境選択可否\s*[:：]\s*未確認",
    }.items():
        if re.search(pat,s): missing.append(label)
    return missing
if __name__=="__main__":
    if len(sys.argv)!=2: sys.exit("usage: python3 scripts/release_instruction.py draft.md")
    try: content=pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    except (OSError,UnicodeError) as e: sys.exit(f"BLOCKED: {e}")
    missing=release(content)
    if missing:
        print("BLOCKED: "+", ".join(missing),file=sys.stderr);sys.exit(1)
    print(content,end="")
