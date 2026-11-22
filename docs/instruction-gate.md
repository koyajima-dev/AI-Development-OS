# Instruction Gate (candidate)
This branch adds a **structural** validator for implementation instructions. It does not verify model availability, official naming, technical safety, or truthfulness.

## Usage
```sh
python3 scripts/instruction_gate.py path/to/complete-instruction.md
python3 -m unittest discover -s tests -p 'test_instruction_gate.py' -v
```

Exit codes: 0 = required textual structure found; 1 = missing structure; 2 or other nonzero = invocation/read failure. Any nonzero result blocks delivery.

## Operational rule
1. Produce a **complete standalone** instruction, not an appendix.
2. Run the structural gate and save its output.
3. Independently verify the **exact model and effort** using official documentation and the actual agent environment. If availability is unknown, stop before execution; do not invent names or silently substitute.
4. Check safety, scope, acceptance, evidence and Human decision boundaries semantically.
5. Only release a verified full instruction after these checks.

## Integration limits
GitHub branch is not evidence of synchronization with the user's local AID OS repository, other projects, or ChatGPT's response generator. GitHub Actions tests this validator on relevant commits, **not** every ChatGPT message. Automatic enforcement in ChatGPT requires a supported invocation path and has not been demonstrated.
