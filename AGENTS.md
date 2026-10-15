# Agent guidelines for Xuling Zhao’s website

Read [DESIGN.md](DESIGN.md) before editing. This is a personal site derived from al-folio v1, not the upstream starter repository. The user’s latest instructions take precedence.

## Workflow

- Check the branch and working tree. Develop on `redesign`; preserve unrelated changes. Commit, merge, push, or publish only within the current task’s authorization.
- Keep the confirmed design and five-item navigation. Public content is English. Do not restore template biographies or fictional work as personal achievements.
- Keep references under `docs/`, excluded from the site. Follow the [maintenance guides](docs/README.md) for actual content.
- Update DESIGN.md when decisions or progress change. Do not duplicate detailed instructions across files.
- When adding or removing a public HTML page, update `test/site-routes.json`. Do not weaken the route check to accept every generated page.

## Runtime ownership

al-folio v1 uses versioned gems for layouts, includes, Sass, Liquid tags, and feature scripts. The personal page wrappers are in `_pages/`; shared styling is in `assets/css/home.css`.

Do not add `_layouts/`, `_includes/`, `_sass/`, `_scripts/`, `assets/tailwind/`, `assets/webfonts/`, or a local Tailwind build pipeline. The style-contract check enforces this boundary. See [ARCHITECTURE.md](docs/ARCHITECTURE.md) and [BOUNDARIES.md](docs/BOUNDARIES.md) for plugin ownership and the distinction between starter and personal-site overrides.

Keep plugin membership in `Gemfile` and `_config.yml` synchronized. A feature requires its gem, site flag, and page opt-in; missing any of these can silently render nothing. Preserve locked dependency versions unless the task needs an update.

## Validation

```bash
npm run lint:prettier
npm run lint:style-contract
git diff --check
```

Build using [LOCAL_DEVELOPMENT.md](docs/LOCAL_DEVELOPMENT.md), then run `python3 bin/check-site.py _site --baseurl /al-folio`. For production output, use `--baseurl ""`. Check desktop and mobile views for layout changes and list/detail/return paths for navigation changes.

The old starter integration tests required deleted demo routes and have been replaced by this personal-site output check. Do not restore their fixtures into the public site. Component tests for gem runtime behavior belong to the owning gem.

## Local and published URLs

- Local: `bash bin/serve-local`, then `http://127.0.0.1:4000/al-folio/`.
- Production: `_config.production.yml` overrides URL and baseurl for `https://xulingzhao.github.io/`.
- Deploy site builds `main` into `gh-pages`; GitHub Pages publishes `gh-pages` root. Keep these stages distinct when diagnosing deployment.

Generated files, screenshots, and logs belong in ignored directories. Never delete `.git`, required `vendor/` dependencies, or `.bundle/github-xulingzhao.pub` during routine cleanup: the latter is referenced by local Git SSH configuration.
