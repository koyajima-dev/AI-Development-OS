# Verified instruction CLI (limited path)

This optional command releases a Markdown draft only if the existing
`scripts/release_instruction.py` accepts it:

```sh
python3 scripts/verified_instruction.py draft.md released.md
```

- The source draft is preserved.
- Existing destination files are never overwritten.
- A rejected draft does not create a release file.
- The existing gate checks structural fields and self-declared confirmation flags,
  **not** the truth of model names, official sources, or environment availability.
- This command does **not** intercept ChatGPT responses, enforce use across projects,
  or establish new-chat compliance. Bypassing this command remains possible.
- The CLI is a candidate pathway, not a universal completion gate.
