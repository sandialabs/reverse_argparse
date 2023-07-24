
# v1.0.2 (2023-07-24)

## Continuous Integration
* ci: Remove `-vv` for `semantic-release` ([`d83ae5d`](https://github.com/sandialabs/reverse_argparse/commit/d83ae5d1063a43de2822ba513b574745eed5a2e9))

## Fix
* fix: Release notes template ([`1ac839a`](https://github.com/sandialabs/reverse_argparse/commit/1ac839a5bf1a252830dd9bf9267bd049031b7f9b))
* fix: Semantic release configuration ([`0325dc0`](https://github.com/sandialabs/reverse_argparse/commit/0325dc0cd5dacee541f495652857fe43c9e1a3fe))

  * Add `__init__.py` to the files modified.
  * Fix the `__version__` in that file.
  * Remove trailing space in CHANGELOG template.
  * Add build command.
  * Make release commit match conventional standard.
  * Add release notes template.
  * Publish releases to PyPI and GitHub Releases.
