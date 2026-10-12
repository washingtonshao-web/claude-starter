---
name: codex-gpt
description: Run a GPT model through the OpenAI Codex CLI/desktop binary when the user asks for GPT, a second opinion, dual-model collaboration, or image generation/editing.
---

# GPT via Codex

Requires the Codex app or CLI installed and signed in. Find the newest binary:

- Windows desktop app: newest `%LOCALAPPDATA%\OpenAI\Codex\bin\*\codex.exe`
- Otherwise: `codex` on PATH (update it if the model below is rejected)

```bash
codex exec -m <model> -c model_reasoning_effort=medium --skip-git-repo-check --ephemeral \
  -s workspace-write -C <dir> --add-dir <outdir> -o <scratchpad>/r.txt "<prompt>" </dev/null
```

`<model>`: the newest GPT model your Codex account offers (check `codex --help` or the app).
Relay `r.txt`, marking what came from GPT.

## Images
Same command, prompt: "Use built-in image_gen at the largest size and highest quality available: <brief, aspect ratio>. Copy PNG to <outdir>/<name>.png; reply path + pixel size."
Default outdir `./images`. Never overwrite. Use `-i <file>` for edits. View the image before delivering.
