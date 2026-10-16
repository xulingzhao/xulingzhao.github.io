# Xuling Zhao

Source for my personal academic website: **<https://xulingzhao.github.io/>**.

I’m an undergraduate at the School of Artificial Intelligence, Nanjing University.
My interests include machine learning and diffusion language models.

The site uses a minimal white background, black text, Fraunces Italic for English, LXGW WenKai for Chinese, and full-color images.
It is built with al-folio v1 and Jekyll, with its runtime supplied by pinned Ruby gems.

## Pages

- **About** — biography, education, research interests, awards, and contact details.
- **Publications** — reserved for my publications; currently empty.
- **Projects** — future Applied and Personal projects; currently empty.
- **Writing** — technical articles and personal reflections, starting with “理解 KL 散度” (October 15, 2026).
- **Notes** — course, reading, and study notes; currently empty.

Template biographies, papers, projects, and posts are not presented as my work.
Old CV, teaching, people, books, news, and repository pages have been removed.

## Preview locally

From this project directory, with the local dependencies installed:

```bash
bash bin/serve-local
```

Open **<http://127.0.0.1:4000/al-folio/>** when the terminal shows `Server running`.
Keep the terminal open. Press **Control + C** to stop; run the same command to start again.
See [local development](docs/LOCAL_DEVELOPMENT.md) for setup and production checks.

## Edit the site

Read [DESIGN.md](DESIGN.md) for the confirmed design, content rules, and current progress.
Agent instructions are in [AGENTS.md](AGENTS.md).

| Location                                | Purpose                                                                |
| --------------------------------------- | ---------------------------------------------------------------------- |
| `_data/home.yml`, `_data/socials.yml`   | Personal information and contact details                               |
| `_pages/`                               | Main pages, Writing archive, and the styled 404 page                   |
| `assets/css/home.css`, `assets/fonts/`  | Shared personal styling and the licensed font                          |
| `_bibliography/publications.bib`        | My publications, currently empty                                       |
| `_projects/`, `_posts/`                 | Create these directories when adding real projects or articles         |
| `docs/`                                 | Maintenance guides and source-only examples; excluded from the website |
| `test/site-routes.json`                 | Explicit list of approved public HTML routes                           |
| `_config.yml`, `_config.production.yml` | Local configuration and production URL overrides                       |

For new content, use the [maintenance guides](docs/README.md) and the archived [personal-style references](docs/site-reference/README.md).
Use real information, replace example links and media, and add each intended public page to `test/site-routes.json`.
The build check rejects unexpected HTML output and broken local links.

## Checks and publishing

```bash
npm run lint:prettier
npm run lint:style-contract
python3 bin/check-site.py _site --baseurl /al-folio
```

Run the site check after a fresh build. Development happens on `redesign`; `main` holds approved releases.
Pushing `main` runs [Deploy site](.github/workflows/deploy.yml), builds the site, checks it, and replaces the generated contents of `gh-pages`.
GitHub **Settings → Pages** must use **Deploy from a branch → gh-pages → /(root)**.
The subsequent **pages build and deployment** run publishes the website. A local edit is not a deployment.

## References and storage

The original project/article examples and sample bibliographies are kept as excluded text references under `docs/`.
Unused demo media, template-only automation, and old generated previews have been removed.
See [cleanup notes](docs/CLEANUP.md) for retained files, recovery, and safe local cleanup.

Built on [al-folio](https://github.com/alshedivat/al-folio) and [Jekyll](https://jekyllrb.com/), hosted on GitHub Pages.
The original code license is retained in [LICENSE](LICENSE). Font sources, versions, and licenses are documented in [FONTS.md](docs/FONTS.md).
