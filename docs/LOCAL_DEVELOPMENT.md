# Local preview on this Mac

This checkout uses al-folio v1, with its layouts and styles supplied by versioned Ruby gems.
The local helper uses Homebrew Ruby, project-local gems in `vendor/`, and Python tools in `.venv/`.
These dependency directories are ignored by Git. Docker is not required for this setup.

The template blog posts and feed configuration are archived under `docs/writing-examples/`.
The helper keeps external feeds disabled in an ignored `.bundle/local-preview.yml` override, so future feed configuration will not require network requests during local preview.
Source content and deployment settings are not rewritten by the helper.
The override also excludes agent configuration directories to avoid duplicate file-watcher warnings from their symlinks.
The helper uses polling for reliable change detection in OneDrive and excludes local dependency directories from the file watcher.

## Start

Open Terminal and run:

```bash
cd "/Users/orion/Library/CloudStorage/OneDrive-个人/文档/Los/Project/website/my-website"
bash bin/serve-local
```

Wait until the terminal shows `Server running`, then open <http://127.0.0.1:4000/al-folio/>.
Keep that terminal open while previewing. Most content edits rebuild automatically; restart the server after editing `_config.yml`.
The preview path follows the existing `baseurl` setting; see [the architecture guide](ARCHITECTURE.md#3-this-repos-effective-baseurl-is-al-folio).

## Production URL

The GitHub Pages deployment workflow adds `_config.production.yml` to build for `https://xulingzhao.github.io/` at the domain root. The local helper keeps `/al-folio/`; do not remove that path from the local preview URL.

## Stop

In the terminal running the server, press **Control + C** (not Command + C).
Run the same start command next time. Starting or stopping the preview does not publish the site.

## Reinstall dependencies if needed

The first-time installation uses the existing Homebrew Ruby, Node.js, Python 3, and Xcode Command Line Tools.
ImageMagick generates the template's responsive images; nbconvert renders its example notebooks.
Run these commands from the project directory only if the local dependencies have been removed:

```bash
brew install imagemagick
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
gem install bundler -v 4.0.6 --no-document --install-dir vendor/tooling
export GEM_HOME="$PWD/vendor/tooling"
export BUNDLE_PATH="$PWD/vendor/bundle"
export BUNDLE_FROZEN=true
ruby vendor/tooling/bin/bundle install
python3 -m venv .venv
.venv/bin/python -m pip install nbconvert
```

The frozen setting keeps the committed dependency versions unchanged. For Docker and other setup options, see [INSTALL.md](INSTALL.md).
