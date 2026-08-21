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
| [`no-nonsense`](no-nonsense) | Translate cryptic, convoluted, or over-engineered AI output into plain English. |

## Follow-ups

- **codebase-diagram spec cleanup.** `render.py` and `template.html` sit at the skill root; the spec puts scripts in `scripts/` and static resources in `assets/`. Move them in a later pass. `CHANGELOG.md` and `VERSION` are non-spec extras kept as a repo convention.

## License

MIT — see [LICENSE](LICENSE).
