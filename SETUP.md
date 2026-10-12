# Setup instructions (for Claude to follow)

You are setting up the user's own Claude Code environment from this starter repo. Nothing here is personal to the repo author.
Work in the cloned repo folder; write only to `~/.claude` (and `~/.codex` if asked). Back up before overwriting.

## Step 1 - Ask once
Ask ONE batch of at most 5 questions, each with a default in brackets:
1. What name and language(s) should I use for you (e.g. English; English + Chinese voice dictation)? [English]
2. Which OS, and where should temporary files go? [detect OS; ~/tmp or %TEMP%]
3. Auto-commit and push finished, verified work without asking? [no]
4. Extras: `codex-gpt` (GPT second opinion/images; needs Codex installed) and the `deep-research` workflow? [deep-research yes; codex-gpt only if Codex is installed]
5. Do you also use Codex (then also create ~/.codex/AGENTS.md and copy skills)? [no]

## Step 2 - Generate instructions
- Read `templates/CLAUDE.template.md`. Fill `{{NAME}}`, `{{LANGUAGE_NOTE}}`, `{{TEMP_DIR}}`.
- Remove the `OPTIONAL:AUTOCOMMIT` block if the answer to Q3 is no. Remove `OPTIONAL:PATHS` if the user has no temp-dir preference. Remove all marker comments.
- If `~/.claude/CLAUDE.md` exists, summarise the differences and back it up to `~/.claude-starter-backup/<timestamp>/` before writing.
- If Q5 is yes, do the same with `templates/AGENTS.template.md` -> `~/.codex/AGENTS.md`.

## Step 3 - Install skills and workflows
Run `python -I scripts/install.py --skills <chosen> --workflows <chosen> [--codex]` (try `--dry-run` first).

## Step 4 - Never copy
Anyone else's memory, keys, tokens or account settings. `deep-research` needs nothing extra. `codex-gpt` needs the Codex app or CLI signed in.

## Step 5 - Report
Finish with a checklist of installed files and what the user must do by hand: sign in to Codex if used; add connectors such as Gmail in claude.ai -> Settings -> Connectors; restart Claude so new skills load.
