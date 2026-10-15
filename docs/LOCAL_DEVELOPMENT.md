# Local preview on this Mac

This site uses Homebrew Ruby and project-local gems in `vendor/`. Node.js provides formatting checks; Python 3 runs the output audit using only its standard library. Docker and a Python virtual environment are not needed.

## Start and stop

From the project directory:

```bash
bash bin/serve-local
```

When `Server running` appears, open **<http://127.0.0.1:4000/al-folio/>**.
Keep the terminal open. Press **Control + C** to stop. Run the same command next time.
Most content changes rebuild automatically; restart after changing `_config.yml`.

The helper selects Homebrew Ruby, uses ignored local dependencies, disables external feeds for preview, and uses polling for OneDrive file watching. It writes `.bundle/local-preview.yml`; it does not rewrite tracked configuration.

## Reinstall dependencies if needed

Use an existing Homebrew Ruby, Node.js, Python 3, and Xcode Command Line Tools. ImageMagick is needed when adding responsive images.

```bash
brew install imagemagick
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
gem install bundler -v 4.0.6 --no-document --install-dir vendor/tooling
export GEM_HOME="$PWD/vendor/tooling"
export BUNDLE_PATH="$PWD/vendor/bundle"
export BUNDLE_FROZEN=true
ruby vendor/tooling/bin/bundle install
npm ci
```

On Intel Macs, use `/usr/local/opt/ruby/bin` instead. Keep the committed lockfiles unchanged during routine installation.

## Build and verify

From the project directory, set the Ruby environment:

```bash
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
export GEM_HOME="$PWD/vendor/tooling"
export BUNDLE_PATH="$PWD/vendor/bundle"
export BUNDLE_FROZEN=true
```

For local output, stop the preview server before rebuilding `_site`:

```bash
ruby vendor/tooling/bin/bundle exec jekyll build
python3 bin/check-site.py _site --baseurl /al-folio
```

For a separate production check:

```bash
JEKYLL_ENV=production ruby vendor/tooling/bin/bundle exec jekyll build --config _config.yml,_config.production.yml --destination .bundle/production-check
python3 bin/check-site.py .bundle/production-check --baseurl ""
```

Also run `npm run lint:prettier`, `npm run lint:style-contract`, and `git diff --check`.
The route manifest is `test/site-routes.json`: add intended new detail pages or pagination URLs when adding real content. Unexpected HTML and broken local links fail the check.

## Publishing

The production configuration serves **<https://xulingzhao.github.io/>** at the domain root; local preview retains `/al-folio/`.
Pushing approved changes to `main` triggers `Deploy site`, which builds and checks output, then replaces the generated files in `gh-pages`.

In GitHub **Settings → Pages**, use **Deploy from a branch → gh-pages → /(root)**. Do not select source `main`: GitHub’s default Jekyll builder cannot load this site's custom gems.
Check both `Deploy site` and the subsequent `pages build and deployment` run. Removed routes disappear from the live website only after successful deployment; the historical Actions failures remain historical records.
