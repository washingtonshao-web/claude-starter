# claude-starter

A small, neutral starting kit for Claude Code (and optionally Codex): general working-style instructions, a GPT second-opinion skill and a deep-research workflow. No personal memory, keys or accounts.

## Use it
Open Claude Code in any folder and paste:

```
Please set up my Claude Code environment from this starter repo: https://github.com/washingtonshao-web/claude-starter
Clone it, read SETUP.md, and follow it exactly. Ask me the one batch of questions first.
```

## Contents
| Path | What |
|---|---|
| `SETUP.md` | Step-by-step instructions Claude follows |
| `templates/CLAUDE.template.md`, `AGENTS.template.md` | Instruction templates with placeholders and optional blocks |
| `skills/codex-gpt` | Ask GPT via the Codex CLI/app for a second opinion or images |
| `workflows/deep-research.js` | Multi-agent research workflow with independent review |
| `scripts/install.py` | Backup-first installer used by SETUP.md |

---
中文：这是一个精简、中立的 Claude Code 起步包。把上面的提示词粘贴给你的 Claude，它会先问你几个问题（语言、是否自动提交、要装哪些扩展），再按你的偏好生成自己的 CLAUDE.md 并安装技能，不会复制任何别人的记忆、密钥或账号。
