# skills

A catalogue of agent skills I've found useful.

## Install the whole catalogue

```bash
npx skills add elliottlawson/skills -g -a opencode
```

Swap `opencode` for `cursor` or `claude` to install into those agents.

## Try one skill without installing

```bash
npx skills use elliottlawson/skills@no-nonsense
```

This prints the skill as a prompt you can paste into any agent. Handy for testing a skill before you commit to it.

## The catalogue

| Skill | What it does |
|---|---|
| [`codebase-diagram`](codebase-diagram) | Generates an interactive visual diagram from a codebase. |
| [`no-nonsense`](no-nonsense) | Instructs your agent to use plain English instead of "agentspeak", i.e. cryptic, convoluted, over-engineered output. |
| [`writing-craft`](writing-craft) | Write or rewrite any document so every line works toward its goal. |

## License

MIT — see [LICENSE](LICENSE).