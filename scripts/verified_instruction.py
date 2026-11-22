#!/usr/bin/env python3
"""Fail-closed CLI for releasing a draft via the existing release gate.

Scope: this command only. Does not intercept ChatGPT chat output.
"""
import argparse
import pathlib
import subprocess
import sys


def publish(source: pathlib.Path, destination: pathlib.Path, root: pathlib.Path) -> int:
    if source.resolve() == destination.resolve():
        print("BLOCKED: source and destination must differ", file=sys.stderr)
        return 2
    if destination.exists():
        print("BLOCKED: destination exists; no overwrite", file=sys.stderr)
        return 2
    gate = root / "scripts" / "release_instruction.py"
    if not gate.is_file():
        print("BLOCKED: existing release gate not found", file=sys.stderr)
        return 2
    result = subprocess.run([sys.executable, str(gate), str(source)], capture_output=True)
    if result.returncode:
        sys.stderr.buffer.write(result.stderr or result.stdout or b"BLOCKED: validation failed\n")
        return result.returncode
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as output:
            output.write(result.stdout)
    except OSError as exc:
        print(f"BLOCKED: could not publish: {exc}", file=sys.stderr)
        return 2
    print(f"PASS: released through verified CLI path: {destination}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()
    return publish(args.draft, args.output, pathlib.Path(__file__).resolve().parents[1])


if __name__ == "__main__":
    raise SystemExit(main())
