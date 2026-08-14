# skills

Agent skills by Elliott Lawson. [Agent Skills spec](https://agentskills.io)-compatible — each skill is a directory with a `SKILL.md` that any compliant agent client (OpenCode, Cursor, Claude Code, …) can load.

Skills land here one at a time, when they're ready. Each one is iterated privately first and published deliberately — watch the repo if you want the drops.

## Install

```bash
npx skills add elliottlawson/skills -g -a opencode   # or -a cursor, -a claude, …
```

Or clone and copy the skill directories you want into your client's skills path (e.g. `~/.agents/skills/`).

## Skills

| Skill | What it does |
|---|---|
| [`codebase-diagram`](codebase-diagram) | Turn a codebase into an interactive visual system diagram — isometric structures, animated data flows, inspect panel. |

## License

MIT — see [LICENSE](LICENSE).
