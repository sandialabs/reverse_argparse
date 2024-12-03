# CHANGELOG



## v2.0.0 (2024-12-03)

### Chores
* chore!: Drop support for Python 3.8 ([`5c448ec`](https://github.com/sandialabs/reverse_argparse/commit/5c448ec9e02cbb61d7f9872730b7c9b40a731035))

  * Use the type-hinting provided out of the box in 3.9.
  * Remove version guards around `argparse.BooleanOptionalAction`.
  * Update documentation and CI accordingly.
* chore(deps): Bump python-semantic-release/python-semantic-release ([`ac3702c`](https://github.com/sandialabs/reverse_argparse/commit/ac3702c574b61d4e056233cfa0f0bb7ea210b6be))

  Bumps the github-actions-dependencies group with 1 update: [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).


  Updates `python-semantic-release/python-semantic-release` from 9.14.0 to 9.15.0
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/825655a47c9f7496f99ab144d28c424d40333a8a...2773f6d901a5cefed959c6ccda302ef41fed67dc)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 4 updates ([`7f8c1df`](https://github.com/sandialabs/reverse_argparse/commit/7f8c1dfd3a3f4bf25d15aa72299f2686a57156ab))

  Bumps the github-actions-dependencies group with 4 updates: [step-security/harden-runner](https://github.com/step-security/harden-runner), [github/codeql-action](https://github.com/github/codeql-action), [codecov/codecov-action](https://github.com/codecov/codecov-action) and [actions/dependency-review-action](https://github.com/actions/dependency-review-action).


  Updates `step-security/harden-runner` from 2.10.1 to 2.10.2
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/91182cccc01eb5e619899d80e4e971d6181294a7...0080882f6c36860b6ba35c610c98ce87d4e2f26f)

  Updates `github/codeql-action` from 3.27.4 to 3.27.5
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/ea9e4e37992a54ee68a9622e985e60c8e8f12d9f...f09c1c0a94de965c15400f5634aa42fac8fb8f88)

  Updates `codecov/codecov-action` from 5.0.2 to 5.0.7
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/5c47607acb93fed5485fdbf7232e8a31425f672a...015f24e6818733317a2da2edd6290ab26238649a)

  Updates `actions/dependency-review-action` from 4.4.0 to 4.5.0
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/4081bf99e2866ebe428fc0477b69eb4fcda7220a...3b139cfc5fae8b618d3eae3675e383bb1769c019)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 3 updates ([`dc2383e`](https://github.com/sandialabs/reverse_argparse/commit/dc2383e9fa5422a1695c28ecbdd2015b29f07bd1))

  Bumps the github-actions-dependencies group with 3 updates: [github/codeql-action](https://github.com/github/codeql-action), [codecov/codecov-action](https://github.com/codecov/codecov-action) and [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).


  Updates `github/codeql-action` from 3.27.1 to 3.27.4
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/4f3212b61783c3c68e8309a0f18a699764811cda...ea9e4e37992a54ee68a9622e985e60c8e8f12d9f)

  Updates `codecov/codecov-action` from 4.6.0 to 5.0.2
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/b9fd7d16f6d7d1b5d2bec1a2887e65ceed900238...5c47607acb93fed5485fdbf7232e8a31425f672a)

  Updates `python-semantic-release/python-semantic-release` from 9.13.0 to 9.14.0
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/adfd8f647244e9bb2d5e8303cc053cc08e6ff41a...825655a47c9f7496f99ab144d28c424d40333a8a)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-major
    dependency-group: github-actions-dependencies
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 3 updates ([`dc6341e`](https://github.com/sandialabs/reverse_argparse/commit/dc6341e8a57baebc99bbff544c5ea25ed0e5a7ab))

  Bumps the github-actions-dependencies group with 3 updates: [github/codeql-action](https://github.com/github/codeql-action), [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) and [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish).


  Updates `github/codeql-action` from 3.27.0 to 3.27.1
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/662472033e021d55d94146f66f6058822b0b39fd...4f3212b61783c3c68e8309a0f18a699764811cda)

  Updates `python-semantic-release/python-semantic-release` from 9.12.0 to 9.13.0
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/c1bcfdbb994243ac7cf419365d5894d6bfb2950e...adfd8f647244e9bb2d5e8303cc053cc08e6ff41a)

  Updates `pypa/gh-action-pypi-publish` from 1.11.0 to 1.12.2
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/fb13cb306901256ace3dab689990e13a5550ffaa...15c56dba361d8335944d31a2ecd17d700fc7bcbc)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 2 updates ([`4570ba6`](https://github.com/sandialabs/reverse_argparse/commit/4570ba6948ee956467e17428dc023cd14c2e378a))

  Bumps the github-actions-dependencies group with 2 updates: [actions/dependency-review-action](https://github.com/actions/dependency-review-action) and [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish).


  Updates `actions/dependency-review-action` from 4.3.5 to 4.4.0
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/a6993e2c61fd5dc440b409aa1d6904921c5e1894...4081bf99e2866ebe428fc0477b69eb4fcda7220a)

  Updates `pypa/gh-action-pypi-publish` from 1.10.3 to 1.11.0
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/f7600683efdcb7656dec5b29656edb7bc586e597...fb13cb306901256ace3dab689990e13a5550ffaa)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 4 updates ([`547feb7`](https://github.com/sandialabs/reverse_argparse/commit/547feb7f601cb4ec2014ddfc2bbb185b178273bb))

  Bumps the github-actions-dependencies group with 4 updates: [actions/checkout](https://github.com/actions/checkout), [github/codeql-action](https://github.com/github/codeql-action), [actions/setup-python](https://github.com/actions/setup-python) and [actions/dependency-review-action](https://github.com/actions/dependency-review-action).


  Updates `actions/checkout` from 4.2.1 to 4.2.2
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871...11bd71901bbe5b1630ceea73d27597364c9af683)

  Updates `github/codeql-action` from 3.26.13 to 3.27.0
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/f779452ac5af1c261dce0346a8f964149f49322b...662472033e021d55d94146f66f6058822b0b39fd)

  Updates `actions/setup-python` from 5.2.0 to 5.3.0
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/f677139bbe7f9c59b41e40162b753c062f5d49a3...0b93645e9fea7318ecaed2b359559ac225c90a2b)

  Updates `actions/dependency-review-action` from 4.3.4 to 4.3.5
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/5a2ce3f5b92ee19cbb1541a4984c76d921601d7c...a6993e2c61fd5dc440b409aa1d6904921c5e1894)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`4169858`](https://github.com/sandialabs/reverse_argparse/commit/4169858725607f24fa874a91e08c81e4e508770d))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.11.1 to 9.12.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/657118d28ae4a74d8a387bedf5db2bb7bac0cb33...c1bcfdbb994243ac7cf419365d5894d6bfb2950e)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore: Tweak dependabot again ([`1af1398`](https://github.com/sandialabs/reverse_argparse/commit/1af139888af3580b53bef3f3a5c2f7bbfc47728a))
* chore(deps): Bump taskmedia/action-conventional-commits ([`e353030`](https://github.com/sandialabs/reverse_argparse/commit/e353030be1a9e014982554cab5fa8b5bd316dbf7))

  Bumps [taskmedia/action-conventional-commits](https://github.com/taskmedia/action-conventional-commits) from 1.1.18 to 1.1.19.
  - [Release notes](https://github.com/taskmedia/action-conventional-commits/releases)
  - [Changelog](https://github.com/taskmedia/action-conventional-commits/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/taskmedia/action-conventional-commits/compare/180c46eb0f4380691dc9845e68b1ef36c05d57d7...cb0de258e7309e163ee353a8c38e24e609608cd6)

  ---
  updated-dependencies:
  - dependency-name: taskmedia/action-conventional-commits
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`7107f0c`](https://github.com/sandialabs/reverse_argparse/commit/7107f0c098678cc5167f8c0c2be0d785cfb96290))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.11.0 to 9.11.1.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/ce77b7cf8cd82f06a01a17f0c57e9e6055f96cce...657118d28ae4a74d8a387bedf5db2bb7bac0cb33)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.12 to 3.26.13 ([`f5b2806`](https://github.com/sandialabs/reverse_argparse/commit/f5b280677c828baaded7f155ee0bb291449ce521))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.12 to 3.26.13.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/c36620d31ac7c881962c3d9dd939c40ec9434f2b...f779452ac5af1c261dce0346a8f964149f49322b)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`50f3886`](https://github.com/sandialabs/reverse_argparse/commit/50f38866d45e8d410ce1bc3bf16867aa41225091))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.10.1 to 9.11.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/d6ea6b856fc884559d9f66b4d9a7dd643fc82c6a...ce77b7cf8cd82f06a01a17f0c57e9e6055f96cce)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore: Tweak dependabot ([`c4c9252`](https://github.com/sandialabs/reverse_argparse/commit/c4c9252c6f060c8eee3b4ea5878710d2a96243e6))

  Run weekly instead of daily, and group updates into a single PR for each
  packaging ecosystem.
* chore(deps): Bump actions/upload-artifact from 4.4.2 to 4.4.3 ([`6add005`](https://github.com/sandialabs/reverse_argparse/commit/6add005a53a430236957ce9bf7021b2d00cbf16b))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.4.2 to 4.4.3.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/84480863f228bb9747b473957fcc9e309aa96097...b4b15b8c7c6ac21ea08fcf65892d2ee8f75cf882)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`32738aa`](https://github.com/sandialabs/reverse_argparse/commit/32738aa300e50f9f9ee9fdb52ad365548db7a0e6))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.10.0 to 9.10.1.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/18399a7209118c6f0bcc923857ef7052cc5de5e3...d6ea6b856fc884559d9f66b4d9a7dd643fc82c6a)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`5e16115`](https://github.com/sandialabs/reverse_argparse/commit/5e16115d76b1f8bc371863cbcdf226c161e99756))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.9.0 to 9.10.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/fd8c509df1f16daf3f71a9a6fac49247017017b2...18399a7209118c6f0bcc923857ef7052cc5de5e3)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.4.1 to 4.4.2 ([`354b5ab`](https://github.com/sandialabs/reverse_argparse/commit/354b5abf942361b86e1b88cc5a1309863ac41d66))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.4.1 to 4.4.2.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/604373da6381bf24206979c74d06a550515601b9...84480863f228bb9747b473957fcc9e309aa96097)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.11 to 3.26.12 ([`7f97c70`](https://github.com/sandialabs/reverse_argparse/commit/7f97c701acccf10ad17c233ef014b747cd0488c0))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.11 to 3.26.12.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/6db8d6351fd0be61f9ed8ebd12ccd35dcec51fea...c36620d31ac7c881962c3d9dd939c40ec9434f2b)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 4.2.0 to 4.2.1 ([`73bfffc`](https://github.com/sandialabs/reverse_argparse/commit/73bfffc3f42b5f6d0909709956a5eb6be0b7fddc))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 4.2.0 to 4.2.1.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/d632683dd7b4114ad314bca15554477dd762a938...eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.4.0 to 4.4.1 ([`ae7c6a4`](https://github.com/sandialabs/reverse_argparse/commit/ae7c6a45c78e92e6f4105e491f5298d69888e44e))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.4.0 to 4.4.1.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/50769540e7f4bd5e21e526ee35c689e35e0d6874...604373da6381bf24206979c74d06a550515601b9)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.10 to 3.26.11 ([`f2b1a33`](https://github.com/sandialabs/reverse_argparse/commit/f2b1a33568c877ee6b512c59c9767b22c51eb300))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.10 to 3.26.11.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/e2b3eafc8d227b0241d48be5f425d47c2d750a13...6db8d6351fd0be61f9ed8ebd12ccd35dcec51fea)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.2 to 1.10.3 ([`f299cb2`](https://github.com/sandialabs/reverse_argparse/commit/f299cb2bd1ddb777bf5425262a914a85f947a23d))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.2 to 1.10.3.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/897895f1e160c830e369f9779632ebc134688e1b...f7600683efdcb7656dec5b29656edb7bc586e597)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump codecov/codecov-action from 4.5.0 to 4.6.0 ([`67ae775`](https://github.com/sandialabs/reverse_argparse/commit/67ae775b4f5eb99d1c774efc2d8eac319a0c16a1))

  Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 4.5.0 to 4.6.0.
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/e28ff129e5465c2c0dcc6f003fc735cb6ae0c673...b9fd7d16f6d7d1b5d2bec1a2887e65ceed900238)

  ---
  updated-dependencies:
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.9 to 3.26.10 ([`a9b4b2e`](https://github.com/sandialabs/reverse_argparse/commit/a9b4b2ef5f41296ebcb9ebf4427d81cdd188398f))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.9 to 3.26.10.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/461ef6c76dfe95d5c364de2f431ddbd31a417628...e2b3eafc8d227b0241d48be5f425d47c2d750a13)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`240eb3a`](https://github.com/sandialabs/reverse_argparse/commit/240eb3affdac6d8a7eefb089bd7917255ee3150d))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.8 to 9.8.9.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/fa2bbbf8e61069551abd513fdc5627e14c8637c7...0a92b5d7ebfc15a84f9801ebd1bf706343d43711)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`1f09b17`](https://github.com/sandialabs/reverse_argparse/commit/1f09b1737cff3ecbc668837ed3e42eb34bbb6dc4))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.8 to 9.9.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/fe6b271e942115b528c85e42bc19611b01dcea59...fd8c509df1f16daf3f71a9a6fac49247017017b2)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 4.1.7 to 4.2.0 ([`6ee990b`](https://github.com/sandialabs/reverse_argparse/commit/6ee990bf75aa79f650f72110f8a75d12fa3f314c))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 4.1.7 to 4.2.0.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/692973e3d937129bcbf40652eb9f2f61becf3332...d632683dd7b4114ad314bca15554477dd762a938)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.8 to 3.26.9 ([`d81149e`](https://github.com/sandialabs/reverse_argparse/commit/d81149e752d7ed7b7aa7b8561a3428d5163e8c6a))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.8 to 3.26.9.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/294a9d92911152fe08befb9ec03e240add280cb3...461ef6c76dfe95d5c364de2f431ddbd31a417628)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.1 to 1.10.2 ([`67ba12f`](https://github.com/sandialabs/reverse_argparse/commit/67ba12fbfd69c1e10914fcd6e9dfc3c2cd94ffc3))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.1 to 1.10.2.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/0ab0b79471669eb3a4d647e625009c62f9f3b241...897895f1e160c830e369f9779632ebc134688e1b)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.7 to 3.26.8 ([`117ae13`](https://github.com/sandialabs/reverse_argparse/commit/117ae137667c4b279cbe19e013368be500c0b647))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.7 to 3.26.8.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/8214744c546c1e5c8f03dde8fab3a7353211988d...294a9d92911152fe08befb9ec03e240add280cb3)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump taskmedia/action-conventional-commits ([`e7e39a9`](https://github.com/sandialabs/reverse_argparse/commit/e7e39a99f0e61104187fcb3c27a8964a231ae68a))

  Bumps [taskmedia/action-conventional-commits](https://github.com/taskmedia/action-conventional-commits) from 1.1.17 to 1.1.18.
  - [Release notes](https://github.com/taskmedia/action-conventional-commits/releases)
  - [Changelog](https://github.com/taskmedia/action-conventional-commits/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/taskmedia/action-conventional-commits/compare/866c0e6dba6aaaef9ad0939a40620b27888906c2...180c46eb0f4380691dc9845e68b1ef36c05d57d7)

  ---
  updated-dependencies:
  - dependency-name: taskmedia/action-conventional-commits
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.6 to 3.26.7 ([`73865f0`](https://github.com/sandialabs/reverse_argparse/commit/73865f0e6869a39265891ea4219fcc7ca7a241d4))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.6 to 3.26.7.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/4dd16135b69a43b6c8efb853346f8437d92d3c93...8214744c546c1e5c8f03dde8fab3a7353211988d)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.10.0 to 2.10.1 ([`33e4124`](https://github.com/sandialabs/reverse_argparse/commit/33e4124086a5b4fff134d338213feb378ec78eed))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.10.0 to 2.10.1.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/446798f8213ac2e75931c1b0769676d927801858...91182cccc01eb5e619899d80e4e971d6181294a7)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.9.1 to 2.10.0 ([`fc185b1`](https://github.com/sandialabs/reverse_argparse/commit/fc185b159262a5bddab366f0f9cc14119616e0c8))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.9.1 to 2.10.0.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/5c7944e73c4c2a096b17a9cb74d65b6c2bbafbde...446798f8213ac2e75931c1b0769676d927801858)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`237ab63`](https://github.com/sandialabs/reverse_argparse/commit/237ab63b40c689a0f16a682e62b857b06df5f617))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.7 to 9.8.8.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/17c75b706f81263690a0a0dc88d83415f783fc04...fa2bbbf8e61069551abd513fdc5627e14c8637c7)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.0 to 1.10.1 ([`7a2cfe6`](https://github.com/sandialabs/reverse_argparse/commit/7a2cfe684c89a0f99d6fe99c4288c796e7c0ec7b))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.0 to 1.10.1.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/8a08d616893759ef8e1aa1f2785787c0b97e20d6...0ab0b79471669eb3a4d647e625009c62f9f3b241)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 5.1.1 to 5.2.0 ([`f4a52fb`](https://github.com/sandialabs/reverse_argparse/commit/f4a52fb7ffd887ec375c5babdb040d3487eb9abe))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5.1.1 to 5.2.0.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/39cd14951b08e74b54015e9e001cdefcf80e669f...f677139bbe7f9c59b41e40162b753c062f5d49a3)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.5 to 3.26.6 ([`dfd64ae`](https://github.com/sandialabs/reverse_argparse/commit/dfd64ae30c5725209d0fbc5474542cf003e22ce2))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.5 to 3.26.6.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/2c779ab0d087cd7fe7b826087247c2c81f27bfa6...4dd16135b69a43b6c8efb853346f8437d92d3c93)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.6 to 4.4.0 ([`81c1e8d`](https://github.com/sandialabs/reverse_argparse/commit/81c1e8df5aa5c34c1558119f29ebb08d382f883d))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.6 to 4.4.0.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/834a144ee995460fba8ed112a2fc961b36a5ec5a...50769540e7f4bd5e21e526ee35c689e35e0d6874)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.0 ([`ddf0aee`](https://github.com/sandialabs/reverse_argparse/commit/ddf0aeea61ef87eff8938daf70ddef7323eb9a2e))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.9.0 to 1.10.0.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/ec4db0b4ddc65acdf4bff5fa45ac92d78b56bdf0...8a08d616893759ef8e1aa1f2785787c0b97e20d6)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`452bf10`](https://github.com/sandialabs/reverse_argparse/commit/452bf105cc387547760307a4cefee14eb07b0fd7))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.7 to 9.8.8.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/708671d0eb33bcbea78c5a3d81ae04c60deeddf3...fe6b271e942115b528c85e42bc19611b01dcea59)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.4 to 3.26.5 ([`c749bf0`](https://github.com/sandialabs/reverse_argparse/commit/c749bf04d0f9fcafdd2ff5c49d1330cd2727d5e2))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.4 to 3.26.5.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/f0f3afee809481da311ca3a6ff1ff51d81dbeb24...2c779ab0d087cd7fe7b826087247c2c81f27bfa6)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.3 to 3.26.4 ([`8be1ae9`](https://github.com/sandialabs/reverse_argparse/commit/8be1ae915df945763e8a7fed7b319968683a0f9a))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.3 to 3.26.4.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/883d8588e56d1753a8a58c1c86e88976f0c23449...f0f3afee809481da311ca3a6ff1ff51d81dbeb24)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`20c5e92`](https://github.com/sandialabs/reverse_argparse/commit/20c5e92740a5bd62adcad8342d914ff630115c9b))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.6 to 9.8.7.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/0dcddac3ba7b691d7a3fd4586b640d7b214a0016...17c75b706f81263690a0a0dc88d83415f783fc04)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`cb96914`](https://github.com/sandialabs/reverse_argparse/commit/cb969147162ce7b18cc53db6a334b214c3338521))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.6 to 9.8.7.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/dec06aa649fddae6610bc64878868498bfcbad7b...708671d0eb33bcbea78c5a3d81ae04c60deeddf3)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.2 to 3.26.3 ([`ed65be0`](https://github.com/sandialabs/reverse_argparse/commit/ed65be03d7db92856c3e78b00f05cd77654712c1))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.2 to 3.26.3.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/429e1977040da7a23b6822b13c129cd1ba93dbb2...883d8588e56d1753a8a58c1c86e88976f0c23449)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.1 to 3.26.2 ([`88dcbaa`](https://github.com/sandialabs/reverse_argparse/commit/88dcbaa52267efb56f45903d01c251b016097cf5))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.1 to 3.26.2.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/29d86d22a34ea372b1bbf3b2dced2e25ca6b3384...429e1977040da7a23b6822b13c129cd1ba93dbb2)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.0 to 3.26.1 ([`baea472`](https://github.com/sandialabs/reverse_argparse/commit/baea47273674cc7f9bd79b8565ab1bdd393c8d70))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.0 to 3.26.1.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/eb055d739abdc2e8de2e5f4ba1a8b246daa779aa...29d86d22a34ea372b1bbf3b2dced2e25ca6b3384)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.15 to 3.26.0 ([`70daaf0`](https://github.com/sandialabs/reverse_argparse/commit/70daaf06824a95b19a33707d12e543a66a204d53))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.15 to 3.26.0.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/afb54ba388a7dca6ecae48f608c4ff05ff4cc77a...eb055d739abdc2e8de2e5f4ba1a8b246daa779aa)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.5 to 4.3.6 ([`c0d5be4`](https://github.com/sandialabs/reverse_argparse/commit/c0d5be4d6bf16877055abb8e6d6db3fee301e0fe))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.5 to 4.3.6.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/89ef406dd8d7e03cfd12d9e0a4a378f454709029...834a144ee995460fba8ed112a2fc961b36a5ec5a)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.9.0 to 2.9.1 ([`0619d28`](https://github.com/sandialabs/reverse_argparse/commit/0619d28a58d289a5f9c0beaaf99c013eff3fb2c7))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.9.0 to 2.9.1.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/0d381219ddf674d61a7572ddd19d7941e271515c...5c7944e73c4c2a096b17a9cb74d65b6c2bbafbde)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.4 to 4.3.5 ([`7ce3a02`](https://github.com/sandialabs/reverse_argparse/commit/7ce3a02ff5834b023c3ff28300c4d8763c77dfcf))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.4 to 4.3.5.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/0b2256b8c012f0828dc542b3febcab082c67f72b...89ef406dd8d7e03cfd12d9e0a4a378f454709029)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.14 to 3.25.15 ([`b4d6f7e`](https://github.com/sandialabs/reverse_argparse/commit/b4d6f7e8f964b77a5f373756b1f6f3e4e887d044))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.14 to 3.25.15.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/5cf07d8b700b67e235fbb65cbc84f69c0cf10464...afb54ba388a7dca6ecae48f608c4ff05ff4cc77a)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump ossf/scorecard-action from 2.3.3 to 2.4.0 ([`e44ac94`](https://github.com/sandialabs/reverse_argparse/commit/e44ac943dc55ac2b416ad54daf746c1550b8aa90))

  Bumps [ossf/scorecard-action](https://github.com/ossf/scorecard-action) from 2.3.3 to 2.4.0.
  - [Release notes](https://github.com/ossf/scorecard-action/releases)
  - [Changelog](https://github.com/ossf/scorecard-action/blob/main/RELEASE.md)
  - [Commits](https://github.com/ossf/scorecard-action/compare/dc50aa9510b46c811795eb24b2f1ba02a914e534...62b2cac7ed8198b15735ed49ab1e5cf35480ba46)

  ---
  updated-dependencies:
  - dependency-name: ossf/scorecard-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.13 to 3.25.14 ([`fd1f6a1`](https://github.com/sandialabs/reverse_argparse/commit/fd1f6a1cd7a62d810ef95bbcd7c565bebdd55689))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.13 to 3.25.14.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/2d790406f505036ef40ecba973cc774a50395aac...5cf07d8b700b67e235fbb65cbc84f69c0cf10464)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`8e348ef`](https://github.com/sandialabs/reverse_argparse/commit/8e348ef59aaed40e9bd6e43215b0707fbf56f046))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.5 to 9.8.6.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/fe6cc89b43d8cbf0f9ce3285df3f77ff69c9b5d4...0dcddac3ba7b691d7a3fd4586b640d7b214a0016)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`0017c68`](https://github.com/sandialabs/reverse_argparse/commit/0017c686f593363058aacbd290d75ae810ad7131))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.5 to 9.8.6.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/3ba53469e72452e7597dd5c61851e6fbf294420b...dec06aa649fddae6610bc64878868498bfcbad7b)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.12 to 3.25.13 ([`ec38213`](https://github.com/sandialabs/reverse_argparse/commit/ec38213caa80f907209d5ff075f96fee3f4378f9))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.12 to 3.25.13.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/4fa2a7953630fd2f3fb380f21be14ede0169dd4f...2d790406f505036ef40ecba973cc774a50395aac)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.8.1 to 2.9.0 ([`d0fdf3a`](https://github.com/sandialabs/reverse_argparse/commit/d0fdf3ae22cffc72ef117808c162a00e21920f49))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.8.1 to 2.9.0.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/17d0e2bd7d51742c71671bd19fa12bdc9d40a3d6...0d381219ddf674d61a7572ddd19d7941e271515c)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.11 to 3.25.12 ([`2d00d7b`](https://github.com/sandialabs/reverse_argparse/commit/2d00d7bb2a500275dda1b3c3ab7869e82da13dbf))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.11 to 3.25.12.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/b611370bb5703a7efb587f9d136a52ea24c5c38c...4fa2a7953630fd2f3fb380f21be14ede0169dd4f)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/dependency-review-action from 4.3.3 to 4.3.4 ([`11f2283`](https://github.com/sandialabs/reverse_argparse/commit/11f22839f71dfbd799e7011b697e355873f9e936))

  Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 4.3.3 to 4.3.4.
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/72eb03d02c7872a771aacd928f3123ac62ad6d3a...5a2ce3f5b92ee19cbb1541a4984c76d921601d7c)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 5.1.0 to 5.1.1 ([`8947428`](https://github.com/sandialabs/reverse_argparse/commit/89474288751babc51c6c2dea256f7710632d33f6))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5.1.0 to 5.1.1.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/82c7e631bb3cdc910f68e0081d67478d79c6982d...39cd14951b08e74b54015e9e001cdefcf80e669f)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`0da57d8`](https://github.com/sandialabs/reverse_argparse/commit/0da57d82ce49f4408fbe0e49e86e7257829af354))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.4 to 9.8.5.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/ab38ab601e1cc0a20e26d1ab089e0b9d40d7faf0...fe6cc89b43d8cbf0f9ce3285df3f77ff69c9b5d4)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.3 to 4.3.4 ([`e5ea10c`](https://github.com/sandialabs/reverse_argparse/commit/e5ea10c4eec5d567a9d2fef685237cade2497484))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.3 to 4.3.4.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/65462800fd760344b1a7b4382951275a0abb4808...0b2256b8c012f0828dc542b3febcab082c67f72b)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`6b67e19`](https://github.com/sandialabs/reverse_argparse/commit/6b67e198d8bee56ca8cb4c2fa75e56fcc8f3cdb8))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from a2854764c7f77ad43f5e421e5a798bcafd1efc90 to 3ba53469e72452e7597dd5c61851e6fbf294420b.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/a2854764c7f77ad43f5e421e5a798bcafd1efc90...3ba53469e72452e7597dd5c61851e6fbf294420b)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`331ceb2`](https://github.com/sandialabs/reverse_argparse/commit/331ceb2b081345eccefce7b57323244b0ffa2181))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.3 to 9.8.4.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/c7c3b69570cbd3011111d2673d8f07142473a871...ab38ab601e1cc0a20e26d1ab089e0b9d40d7faf0)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 3.1.3 to 4.3.3 ([`441ffd2`](https://github.com/sandialabs/reverse_argparse/commit/441ffd22bb5e9d59a14ad9bddf92159a1433cce9))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 3.1.3 to 4.3.3.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/v3.1.3...65462800fd760344b1a7b4382951275a0abb4808)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`4acdc96`](https://github.com/sandialabs/reverse_argparse/commit/4acdc962751494c0c437b7323e00cf9cb885e708))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from adc0c15810c0b9ee22c43d85d1890b394d49a641 to a2854764c7f77ad43f5e421e5a798bcafd1efc90.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/adc0c15810c0b9ee22c43d85d1890b394d49a641...a2854764c7f77ad43f5e421e5a798bcafd1efc90)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump taskmedia/action-conventional-commits ([`7cccac6`](https://github.com/sandialabs/reverse_argparse/commit/7cccac630578bbd2b9f50283135b684d73c02385))

  Bumps [taskmedia/action-conventional-commits](https://github.com/taskmedia/action-conventional-commits) from 1.1.3 to 1.1.17.
  - [Release notes](https://github.com/taskmedia/action-conventional-commits/releases)
  - [Changelog](https://github.com/taskmedia/action-conventional-commits/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/taskmedia/action-conventional-commits/compare/9148865058f63a6cb560ff4bfd7d534505f43646...866c0e6dba6aaaef9ad0939a40620b27888906c2)

  ---
  updated-dependencies:
  - dependency-name: taskmedia/action-conventional-commits
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump codecov/codecov-action from 3.1.6 to 4.5.0 ([`0f52855`](https://github.com/sandialabs/reverse_argparse/commit/0f52855ab1a8a97f7f2ef80ce725137bf1d355b7))

  Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 3.1.6 to 4.5.0.
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/ab904c41d6ece82784817410c45d8b8c02684457...e28ff129e5465c2c0dcc6f003fc735cb6ae0c673)

  ---
  updated-dependencies:
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore: Update LICENSE/COPYRIGHT info ([`aae82e5`](https://github.com/sandialabs/reverse_argparse/commit/aae82e52fccd0a40dba7fa23e73129b172f63ae7))
* chore(deps): Bump ossf/scorecard-action from 2.3.1 to 2.3.3 ([`e3c70c5`](https://github.com/sandialabs/reverse_argparse/commit/e3c70c57b6de1c19ce4916186b6fe5294381a5a5))

  Bumps [ossf/scorecard-action](https://github.com/ossf/scorecard-action) from 2.3.1 to 2.3.3.
  - [Release notes](https://github.com/ossf/scorecard-action/releases)
  - [Changelog](https://github.com/ossf/scorecard-action/blob/main/RELEASE.md)
  - [Commits](https://github.com/ossf/scorecard-action/compare/0864cf19026789058feabb7e87baa5f140aac736...dc50aa9510b46c811795eb24b2f1ba02a914e534)

  ---
  updated-dependencies:
  - dependency-name: ossf/scorecard-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 2.25.11 to 3.25.11 ([`4ff310f`](https://github.com/sandialabs/reverse_argparse/commit/4ff310f66d8ed4b22bd3a32e654c959a1212260c))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 2.25.11 to 3.25.11.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/v2.25.11...b611370bb5703a7efb587f9d136a52ea24c5c38c)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/dependency-review-action from 2.5.1 to 4.3.3 ([`a11bef8`](https://github.com/sandialabs/reverse_argparse/commit/a11bef88e226bd91c0cfd176640d1f7be7b793b4))

  Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 2.5.1 to 4.3.3.
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/0efb1d1d84fc9633afcdaad14c485cbbc90ef46c...72eb03d02c7872a771aacd928f3123ac62ad6d3a)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 3.6.0 to 4.1.7 ([`d2f1d6f`](https://github.com/sandialabs/reverse_argparse/commit/d2f1d6fbeb93fc2e932d85f02a373e9437f1137d))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 3.6.0 to 4.1.7.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3.6.0...692973e3d937129bcbf40652eb9f2f61becf3332)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 4.7.1 to 5.1.0 ([`c908de0`](https://github.com/sandialabs/reverse_argparse/commit/c908de0d6cdcd88a044f49dabb24b8b1bdc36c30))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 4.7.1 to 5.1.0.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/65d7f2d534ac1bc67fcd62888c5f4f3d2cb2b236...82c7e631bb3cdc910f68e0081d67478d79c6982d)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>

### Continuous integration
* ci: pre-commit auto-update ([`3dc3489`](https://github.com/sandialabs/reverse_argparse/commit/3dc3489ecd98a9bc639f93f4420bb943f1c1573d))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.3 → v0.7.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.3...v0.7.4)
* ci: pre-commit auto-update ([`65a6f19`](https://github.com/sandialabs/reverse_argparse/commit/65a6f1983c195080b8a0f30b578d1fcdb2656efd))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.2 → v0.7.3](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.2...v0.7.3)
* ci: pre-commit auto-update ([`0abfbf4`](https://github.com/sandialabs/reverse_argparse/commit/0abfbf473fd686942899e8fa394373a1f56ae0cd))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.1 → v0.7.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.1...v0.7.2)
* ci: pre-commit auto-update ([`6ef8c2d`](https://github.com/sandialabs/reverse_argparse/commit/6ef8c2d62186c6d2873e331ca0b948e69a8a0896))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.0 → v0.7.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.0...v0.7.1)
  - [github.com/gitleaks/gitleaks: v8.21.1 → v8.21.2](https://github.com/gitleaks/gitleaks/compare/v8.21.1...v8.21.2)
  - [github.com/pre-commit/mirrors-mypy: v1.12.1 → v1.13.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.12.1...v1.13.0)
* ci: pre-commit auto-update ([`e283c2c`](https://github.com/sandialabs/reverse_argparse/commit/e283c2c44a7fb1147a2afb639553e99d8d171eb9))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.9 → v0.7.0](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.9...v0.7.0)
  - [github.com/gitleaks/gitleaks: v8.20.1 → v8.21.1](https://github.com/gitleaks/gitleaks/compare/v8.20.1...v8.21.1)
  - [github.com/pre-commit/mirrors-mypy: v1.11.2 → v1.12.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.2...v1.12.1)
* ci: pre-commit auto-update ([`c852df2`](https://github.com/sandialabs/reverse_argparse/commit/c852df2f6a7795b2963ecb17a820576217c22f41))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.8 → v0.6.9](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.8...v0.6.9)
  - [github.com/gitleaks/gitleaks: v8.19.3 → v8.20.1](https://github.com/gitleaks/gitleaks/compare/v8.19.3...v8.20.1)
  - [github.com/pre-commit/pre-commit-hooks: v4.6.0 → v5.0.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.6.0...v5.0.0)
* ci: pre-commit auto-update ([`6c82643`](https://github.com/sandialabs/reverse_argparse/commit/6c8264325c2c7f87be9df169a8d763ece151a9bf))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.7 → v0.6.8](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.7...v0.6.8)
  - [github.com/gitleaks/gitleaks: v8.19.2 → v8.19.3](https://github.com/gitleaks/gitleaks/compare/v8.19.2...v8.19.3)
* ci: pre-commit auto-update ([`d2bae0a`](https://github.com/sandialabs/reverse_argparse/commit/d2bae0a83a2f3e93bdc06aaefaef2eadc04a4677))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.5 → v0.6.7](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.5...v0.6.7)
* ci: pre-commit auto-update ([`fa57321`](https://github.com/sandialabs/reverse_argparse/commit/fa573216d3fff54a0e4d3cf18b8fa0e1acbafddb))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.4 → v0.6.5](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.4...v0.6.5)
  - [github.com/gitleaks/gitleaks: v8.18.4 → v8.19.2](https://github.com/gitleaks/gitleaks/compare/v8.18.4...v8.19.2)
* ci: pre-commit auto-update ([`d3a4c2e`](https://github.com/sandialabs/reverse_argparse/commit/d3a4c2e78a152174551f1e47720bdf258411919f))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.3 → v0.6.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.3...v0.6.4)
* ci: pre-commit auto-update ([`6cb4a5c`](https://github.com/sandialabs/reverse_argparse/commit/6cb4a5c74e6ab80f16d7e0fe1dedcdf8bbc1c662))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.2 → v0.6.3](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.2...v0.6.3)
  - [github.com/PyCQA/doc8: v1.1.1 → v1.1.2](https://github.com/PyCQA/doc8/compare/v1.1.1...v1.1.2)
* ci: pre-commit auto-update ([`96b371a`](https://github.com/sandialabs/reverse_argparse/commit/96b371a3c618f9a7d615c2b67409594224fe6b46))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.1 → v0.6.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.1...v0.6.2)
  - [github.com/pre-commit/mirrors-mypy: v1.11.1 → v1.11.2](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.1...v1.11.2)
* ci: pre-commit auto-update ([`490f0df`](https://github.com/sandialabs/reverse_argparse/commit/490f0df05fb4ffc8bad24dcfdb851cb79ee7987e))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.7 → v0.6.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.7...v0.6.1)
* ci: pre-commit auto-update ([`9d3be74`](https://github.com/sandialabs/reverse_argparse/commit/9d3be7443c11fc3c90d03d6b8f1fd627d269d43a))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.6 → v0.5.7](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.6...v0.5.7)
* ci: pre-commit auto-update ([`31ccecb`](https://github.com/sandialabs/reverse_argparse/commit/31ccecb1e7620510e81c07de834b6af18ffc1fd1))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.5 → v0.5.6](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.5...v0.5.6)
  - [github.com/pre-commit/mirrors-mypy: v1.11.0 → v1.11.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.0...v1.11.1)
* ci: pre-commit auto-update ([`1f75c05`](https://github.com/sandialabs/reverse_argparse/commit/1f75c055411e9595151adfe75b4c9edaa069e1f0))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.4 → v0.5.5](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.4...v0.5.5)
* ci: pre-commit auto-update ([`5e9730f`](https://github.com/sandialabs/reverse_argparse/commit/5e9730fd339a16766fca0fea9bd807cd9f7f02de))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.2 → v0.5.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.2...v0.5.4)
  - [github.com/pre-commit/mirrors-mypy: v1.10.1 → v1.11.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.10.1...v1.11.0)
* ci: pre-commit auto-update ([`6c9dc20`](https://github.com/sandialabs/reverse_argparse/commit/6c9dc20e5e6e4dafef838be08deac339ee12dcf8))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.1 → v0.5.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.1...v0.5.2)
* ci: pre-commit auto-update ([`745c17a`](https://github.com/sandialabs/reverse_argparse/commit/745c17a99316b71f702e290f62fcf47ea28d7c86))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.0 → v0.5.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.0...v0.5.1)
  - [github.com/gitleaks/gitleaks: v8.16.3 → v8.18.4](https://github.com/gitleaks/gitleaks/compare/v8.16.3...v8.18.4)
* ci: Change documentation coverage file name ([`c487d94`](https://github.com/sandialabs/reverse_argparse/commit/c487d94f28f3a160e8d764cc5a7529fe42d3e744))
* ci: Restrict token permissions ([`dfb85fd`](https://github.com/sandialabs/reverse_argparse/commit/dfb85fdc512526ad4c4513849a3839cb344af369))

  https://github.com/sandialabs/reverse_argparse/security/code-scanning/21
* ci: pre-commit auto-update ([`3411062`](https://github.com/sandialabs/reverse_argparse/commit/3411062598f098394545112ec8ff4c2cc6dac6ad))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.10 → v0.5.0](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.10...v0.5.0)
  - [github.com/pre-commit/mirrors-mypy: v1.10.0 → v1.10.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.10.0...v1.10.1)
* ci: Tweak automated suggestions ([`3a73bda`](https://github.com/sandialabs/reverse_argparse/commit/3a73bdabda6608d9bbc2b7f53c94cd12a3282848))
* ci: Apply security best practices ([`27fd558`](https://github.com/sandialabs/reverse_argparse/commit/27fd5585e7629efed20650c3f134125ccc2efee6))

  Signed-off-by: StepSecurity Bot <bot@stepsecurity.io>
* ci: Don't fix Ruff issues ([`6fb3b58`](https://github.com/sandialabs/reverse_argparse/commit/6fb3b58069d381099d07df0ac4c82d039e2f6e28))

  Remove the `--fix` argument from the `ruff` check in the pre-commit
  configuration.  We don't want automated commits pushed to PRs, because
  we want to encourage contributors to clean up their branches before
  merging.  Additionally, when pre-commit doesn't automatically fix files,
  it shows the user what the issues are, thereby training them to avoid
  them in the future.
* ci: pre-commit auto-update ([`4569007`](https://github.com/sandialabs/reverse_argparse/commit/4569007f24f9e26245a54a067ed0e3467c5d9139))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.9 → v0.4.10](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.9...v0.4.10)
* ci: pre-commit auto-update ([`757151e`](https://github.com/sandialabs/reverse_argparse/commit/757151e5d06971c7b4dc7da648272cdffb9467f3))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.8 → v0.4.9](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.8...v0.4.9)
* ci: pre-commit auto-update ([`5b92015`](https://github.com/sandialabs/reverse_argparse/commit/5b92015afb984a4fbb96ed002612ecd81972fdca))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.7 → v0.4.8](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.7...v0.4.8)
* ci: pre-commit auto-update ([`c673c39`](https://github.com/sandialabs/reverse_argparse/commit/c673c3921954d541b86cad8fd0f6ee0ed8b5b41b))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.5 → v0.4.7](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.5...v0.4.7)
* ci: pre-commit auto-update ([`8bbf5e7`](https://github.com/sandialabs/reverse_argparse/commit/8bbf5e72982f05e66848e61c8b94d6d69be1bb1f))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.4 → v0.4.5](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.4...v0.4.5)
* ci: pre-commit auto-update ([`eedaade`](https://github.com/sandialabs/reverse_argparse/commit/eedaade31256a37336778ab76080867d2866b465))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.3 → v0.4.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.3...v0.4.4)

### Documentation
* docs: Fix highlighting in examples ([`149e48c`](https://github.com/sandialabs/reverse_argparse/commit/149e48c6ef8adabbc11027da17cf88338f3d6318))

  I never noticed when we added the license and copyright information to
  the top of all the source files that we didn't account for the
  lines highlighted in the included examples.  This adjusts things such
  that (1) we don't include all that header stuff when generating the
  docs, and only include the lines of code that are really relevant to
  share on the examples page, and (2) the appropriate lines are
  highlighted.
* docs: Slight tweaks to contributing guidelines ([`6e2ddc9`](https://github.com/sandialabs/reverse_argparse/commit/6e2ddc91c8467d7d6fd58cac13a7c630247348df))

### Testing
* test: Remove unnecessary parentheses ([`7c7d39a`](https://github.com/sandialabs/reverse_argparse/commit/7c7d39a3af7775fe1653bfdb5b6591f28f3b14bf))

  To align with updated ruff rules.
* test: Ignore subprocess warning in test file ([`90e3cad`](https://github.com/sandialabs/reverse_argparse/commit/90e3cad5799f79cc67ef8fe915b5f0f4fd14542b))

  This test file uses `subprocess.run()` to run the examples and check
  their output.  The input to `run()` has been verified and is not a
  security vulnerability.

## v1.0.8 (2024-05-13)

### Chores
* chore: Remove commitizen configuration ([`73ceec1`](https://github.com/sandialabs/reverse_argparse/commit/73ceec1bdb5385744c29cef4eb85385603839ee7))
* chore: Remove commitizen pre-commit hook ([`18c274f`](https://github.com/sandialabs/reverse_argparse/commit/18c274f5b42764b8bca3527bd49841ae7bc920da))

  In order to enable a faster development workflow, remove the commitizen
  pre-commit hook to allow commits messages that don't adhere to the
  Conventional Commits specification.  Commit messages are still checked
  in the Continuous Integration workflow, though, so a branch will need to
  be clean before merging.

### Continuous integration
* ci: pre-commit auto-update ([`31ce94a`](https://github.com/sandialabs/reverse_argparse/commit/31ce94a576e39bf6cad6cdace70030d3af4a7da6))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.2 → v0.4.3](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.2...v0.4.3)
* ci: pre-commit auto-update ([`7438097`](https://github.com/sandialabs/reverse_argparse/commit/74380974d006c6f592955282fd51e75f5db3f4c9))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.1 → v0.4.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.1...v0.4.2)
  - [github.com/pre-commit/mirrors-mypy: v1.9.0 → v1.10.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.9.0...v1.10.0)

### Documentation
* docs: Fix license/copyright text in file ([`1d496c1`](https://github.com/sandialabs/reverse_argparse/commit/1d496c1b20da8ee373f41dd08863db222a15876c))

  Should have been included in b3553415da40949f9ce496ca1363cb69424da791,
  but was overlooked.
* docs: Reword Conventional Commits guidelines ([`6659b11`](https://github.com/sandialabs/reverse_argparse/commit/6659b11ea4d855ec48667c5d0fc904ca9f027dbe))
* docs: Add code lines badge ([`9e4953d`](https://github.com/sandialabs/reverse_argparse/commit/9e4953d7fd43d2f325bfdc66cd6c0c71f5fc454e))

### Patch
* patch: Indicate that the package is typed ([`bd89c55`](https://github.com/sandialabs/reverse_argparse/commit/bd89c55ded9b8d7982ff52b46155e4427ddf629e))

  According to PEP 561, we need to add this file to static type checkers
  can infer the types from the package.

### Testing
* test: Ignore assert warnings in test files ([`01f97d0`](https://github.com/sandialabs/reverse_argparse/commit/01f97d037707378cf2fd7c86390c635dfbd5387b))

## v1.0.7 (2024-04-22)

### Chores
* chore: Ignore security findings in tests/examples ([`f18ece4`](https://github.com/sandialabs/reverse_argparse/commit/f18ece4a69291b96b84a80bd8eea0a5f51697026))
* chore: Switch to Ruff ([`6112943`](https://github.com/sandialabs/reverse_argparse/commit/6112943ca3f2a74c0419d8d2452884dd144c8309))

  Use Ruff to replace a variety of linters/formatters.
* chore: Fix badge URLs ([`2c8dda1`](https://github.com/sandialabs/reverse_argparse/commit/2c8dda1315e1d1297acea0f41a827736258d1950))

  Somehow it looks like some hidden character wound up copy/pasted in the
  middle of the `https`.
* chore: Add PR template ([`eb0b3b8`](https://github.com/sandialabs/reverse_argparse/commit/eb0b3b8da57b0c2a67b4928f4d3ae67890aa5bff))

### Continuous integration
* ci: pre-commit auto-update ([`0b14008`](https://github.com/sandialabs/reverse_argparse/commit/0b14008f4a9d74095ef8d627998eb5166b2c0ed1))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.22.0 → v3.24.0](https://github.com/commitizen-tools/commitizen/compare/v3.22.0...v3.24.0)
* ci: Add OpenSSF Scorecard workflow ([`5f8f3cf`](https://github.com/sandialabs/reverse_argparse/commit/5f8f3cf299ff64890cbcbc9d0a780095edb337da))
* ci: pre-commit auto-update ([`f184590`](https://github.com/sandialabs/reverse_argparse/commit/f1845904079290ee6d44bb920c9a9181f31e71b4))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.21.3 → v3.22.0](https://github.com/commitizen-tools/commitizen/compare/v3.21.3...v3.22.0)
  - [github.com/psf/black: 24.3.0 → 24.4.0](https://github.com/psf/black/compare/24.3.0...24.4.0)
* ci: pre-commit auto-update ([`d91334d`](https://github.com/sandialabs/reverse_argparse/commit/d91334d003d9c6c387dc9951f9d0707fde27798d))

  updates:
  - [github.com/pre-commit/pre-commit-hooks: v4.5.0 → v4.6.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.5.0...v4.6.0)
* ci: pre-commit auto-update ([`43b5104`](https://github.com/sandialabs/reverse_argparse/commit/43b51041bff35b96184899e3ec28af60f05869f4))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.20.0 → v3.21.3](https://github.com/commitizen-tools/commitizen/compare/v3.20.0...v3.21.3)
* ci: pre-commit auto-update ([`60cefa8`](https://github.com/sandialabs/reverse_argparse/commit/60cefa80a5c89ec7e7fb26355ce492d2af1ac3d9))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.18.4 → v3.20.0](https://github.com/commitizen-tools/commitizen/compare/v3.18.4...v3.20.0)
* ci: pre-commit auto-update ([`155240b`](https://github.com/sandialabs/reverse_argparse/commit/155240b6589d5ab9dbda33f1c3e3f9ad3a5f8e43))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.15.0 → v3.18.4](https://github.com/commitizen-tools/commitizen/compare/v3.15.0...v3.18.4)
  - [github.com/pre-commit/mirrors-mypy: v1.8.0 → v1.9.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.8.0...v1.9.0)
  - [github.com/psf/black: 24.2.0 → 24.3.0](https://github.com/psf/black/compare/24.2.0...24.3.0)
  - [github.com/PyCQA/bandit: 1.7.7 → 1.7.8](https://github.com/PyCQA/bandit/compare/1.7.7...1.7.8)
* ci: pre-commit auto-update ([`ef525b7`](https://github.com/sandialabs/reverse_argparse/commit/ef525b71056685d8eac17b49660706cec8307fd1))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.14.1 → v3.15.0](https://github.com/commitizen-tools/commitizen/compare/v3.14.1...v3.15.0)
* ci: pre-commit auto-update ([`5e0e1b4`](https://github.com/sandialabs/reverse_argparse/commit/5e0e1b471594634a92f8952e1ffe9b9628c85437))

  updates:
  - [github.com/psf/black: 24.1.1 → 24.2.0](https://github.com/psf/black/compare/24.1.1...24.2.0)
* ci: pre-commit auto-update ([`b6e239d`](https://github.com/sandialabs/reverse_argparse/commit/b6e239decef5760449850b5e9d27c9b507346538))

  updates:
  - [github.com/commitizen-tools/commitizen: v3.13.0 → v3.14.1](https://github.com/commitizen-tools/commitizen/compare/v3.13.0...v3.14.1)
* ci: auto fixes from pre-commit.com hooks ([`2d05e81`](https://github.com/sandialabs/reverse_argparse/commit/2d05e818be047a42cae0fabd0e42b77b2688c87e))

  for more information, see https://pre-commit.ci
* ci: pre-commit auto-update ([`5150bc1`](https://github.com/sandialabs/reverse_argparse/commit/5150bc19e6fe17acd7f5612146189f0bfdf4d4a1))

  updates:
  - [github.com/psf/black: 23.12.1 → 24.1.1](https://github.com/psf/black/compare/23.12.1...24.1.1)
  - [github.com/PyCQA/bandit: 1.7.6 → 1.7.7](https://github.com/PyCQA/bandit/compare/1.7.6...1.7.7)

### Documentation
* docs: Add docstrings to test/example files ([`f0b7eb9`](https://github.com/sandialabs/reverse_argparse/commit/f0b7eb96cff1cd6a6360b1e9eba0b66c614c6ac1))
* docs: Add OpenSSF Scorecard badge to ReadTheDocs ([`91c5557`](https://github.com/sandialabs/reverse_argparse/commit/91c5557f90b3f4ebd3eb71bd6d030133f4085376))
* docs: Add CodeFactor badge ([`105a394`](https://github.com/sandialabs/reverse_argparse/commit/105a3948b4913ad83e38d718db23e4fecec17150))
* docs: Adopt Conventional Comments ([`9d16c0c`](https://github.com/sandialabs/reverse_argparse/commit/9d16c0cef5b291710e32a57c788dc06669eee1e2))

  Try to encourage effective communication via issues/PRs.
* docs: Update link to latest GMS release ([`af2ce45`](https://github.com/sandialabs/reverse_argparse/commit/af2ce4549133ceb306d3f7516bc58a92b6656817))
* docs: Move copyright/license text to comments ([`b355341`](https://github.com/sandialabs/reverse_argparse/commit/b3553415da40949f9ce496ca1363cb69424da791))

  In all source files, move the copyright and license text from the module
  docstring to comments immediately below it.  This is to avoid processing
  this text when Sphinx is automatically generating documentation from
  docstrings.
* docs: Add contributor license agreement ([`9531c94`](https://github.com/sandialabs/reverse_argparse/commit/9531c944fed6acd3e5a6264343078a97c9e5f581))
* docs: Update copyright text in source files ([`4cba3d0`](https://github.com/sandialabs/reverse_argparse/commit/4cba3d06877911ce93c7ae95b2fbb37960e10111))

  Per guidance from Sandia Technology Transfer, the recommended text from
  the Linux Foundation is insufficient for our purposes.
* docs: Update copyright/license info ([`4d1d42a`](https://github.com/sandialabs/reverse_argparse/commit/4d1d42a140834293289c8cf7123a3230802935bb))

  Update the copyright years in the `LICENSE.md` file and add copyright
  and license information to all source files (part of the Gold level
  OpenSSF Best Practices).
* docs: Add coverage job steps ([`3b20a84`](https://github.com/sandialabs/reverse_argparse/commit/3b20a844bb4912e092d466ec1068726cbf989d56))

  Add steps to the CI job to compute the documentation coverage for the
  package and archive the results.

### Patch
* patch: Force `prefer_short` to be keyword-only ([`f02c7f2`](https://github.com/sandialabs/reverse_argparse/commit/f02c7f2eee4861904d3505fd7a6d2cc0fbc5cfc8))

  Turning on `flake8-boolean-trap` linting via Ruff resulted in the
  following findings:

      reverse_argparse/reverse_argparse.py:242:31:
      FBT002 Boolean default positional argument in function definition
      reverse_argparse/reverse_argparse.py:242:31:
      FBT001 Boolean-typed positional argument in function definition
      Found 2 errors.

  Switching `prefer_short` from a positional to a keyword-only argument
  addresses the problem.

  Note that this is technically a breaking change, but only for a
  "private" method, not in the package's public API.  Therefore the change
  is not registered as a breaking change via Conventional Commit syntax,
  and no major version update will be created.  Instead, this commit will
  force the creation of a patch release.  If users were relying on the
  prior behavior of this internal method, they can simply switch to the
  keyword syntax when calling it.

### Refactoring
* refactor: Address Ruff-specific lint findings ([`076e199`](https://github.com/sandialabs/reverse_argparse/commit/076e19951c8fb2241c85d4da063d166292054f25))
* refactor: Address Pylint findings ([`862bc62`](https://github.com/sandialabs/reverse_argparse/commit/862bc62bee7a61659cb69e668f4a1f1d1e9c0c1f))
* refactor: Ignore particular type error ([`9d412dd`](https://github.com/sandialabs/reverse_argparse/commit/9d412ddc83a6b0ad5ad3acfb5a520eb0df20086b))
* refactor: Remove unnecessary shebang lines ([`a7ae1f6`](https://github.com/sandialabs/reverse_argparse/commit/a7ae1f6813797f48f3889d6b362217c55a853079))
* refactor: Assign exception messages to variables ([`844c71a`](https://github.com/sandialabs/reverse_argparse/commit/844c71ab25ce20ebb22b111524740b2c991f3f29))

  Running `flake8-errmsg` via Ruff yielded the following findings:

      reverse_argparse/reverse_argparse.py:143:17:
      EM102 Exception must not use an f-string literal, assign to variable
      first
      reverse_argparse/reverse_argparse.py:461:17:
      EM102 Exception must not use an f-string literal, assign to variable
      first
      Found 2 errors.

  This changes resolves the issues.
* refactor: Don't override Python builtins ([`9006adb`](https://github.com/sandialabs/reverse_argparse/commit/9006adbeefdbd08237325d91fbdf7ecf952b386d))

### Testing
* test: Use tuples for parametrize variables ([`25d9be8`](https://github.com/sandialabs/reverse_argparse/commit/25d9be8d014f0159c4328594af84fc723fdad6f9))
* test: Use UTC timezone with datetime ([`25ff30f`](https://github.com/sandialabs/reverse_argparse/commit/25ff30ff9c19378108db1cc31f367e0a98e189d9))

  Running `flake8-datetimez` via Ruff yielded the following findings:

      example/test_examples.py:88:25:
      DTZ005 `datetime.datetime.now()` called without a `tz` argument
      example/test_examples.py:89:25:
      DTZ007 Naive datetime constructed using
      `datetime.datetime.strptime()` without %z
      example/test_examples.py:125:13:
      DTZ005 `datetime.datetime.now()` called without a `tz` argument
      example/test_examples.py:126:25:
      DTZ007 Naive datetime constructed using
      `datetime.datetime.strptime()` without %z
      Found 4 errors.

  Specifying timezone info resolves the issues.

## v1.0.6 (2024-01-15)

### Continuous integration
* ci: pre-commit auto-update ([`47bb274`](https://github.com/sandialabs/reverse_argparse/commit/47bb274ce756e0846aef876acc083f363accf223))

  updates:
  - [github.com/PyCQA/flake8: 6.1.0 → 7.0.0](https://github.com/PyCQA/flake8/compare/6.1.0...7.0.0)
* ci: pre-commit auto-update ([`9d3e11a`](https://github.com/sandialabs/reverse_argparse/commit/9d3e11a30ba2981456e86c936e49c1f81310ce71))

  updates:
  - [github.com/pre-commit/mirrors-mypy: v1.7.1 → v1.8.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.7.1...v1.8.0)
  - [github.com/psf/black: 23.11.0 → 23.12.1](https://github.com/psf/black/compare/23.11.0...23.12.1)
  - [github.com/PyCQA/isort: 5.13.0 → 5.13.2](https://github.com/PyCQA/isort/compare/5.13.0...5.13.2)
* ci: pre-commit auto-update ([`48da6a4`](https://github.com/sandialabs/reverse_argparse/commit/48da6a49cfd0c3d28fbcbf91f9344d99d703fbe6))

  updates:
  - [github.com/PyCQA/bandit: 1.7.5 → 1.7.6](https://github.com/PyCQA/bandit/compare/1.7.5...1.7.6)
  - [github.com/PyCQA/isort: 5.12.0 → 5.13.0](https://github.com/PyCQA/isort/compare/5.12.0...5.13.0)
* ci: pre-commit auto-update ([`a5591e4`](https://github.com/sandialabs/reverse_argparse/commit/a5591e4a92dd0ce9fb7b74ea414a7cac0ba88945))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.12.0 → v3.13.0](https://github.com/commitizen-tools/commitizen/compare/3.12.0...v3.13.0)
* ci: pre-commit auto-update ([`5d80e7d`](https://github.com/sandialabs/reverse_argparse/commit/5d80e7d9d79737623b20172c415c8afbf1322eb9))

  updates:
  - [github.com/pre-commit/mirrors-mypy: v1.7.0 → v1.7.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.7.0...v1.7.1)
* ci: pre-commit auto-update ([`bbc7a4e`](https://github.com/sandialabs/reverse_argparse/commit/bbc7a4e78cd5e8caba57fa73775a2d5730dfa7dd))

  updates:
  - [github.com/pre-commit/mirrors-mypy: v1.6.1 → v1.7.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.6.1...v1.7.0)
  - [github.com/psf/black: 23.10.1 → 23.11.0](https://github.com/psf/black/compare/23.10.1...23.11.0)
* ci: pre-commit auto-update ([`4c5b060`](https://github.com/sandialabs/reverse_argparse/commit/4c5b06092015bd0ebddcb248ed45a17cc262041a))

  updates:
  - [github.com/psf/black: 23.10.0 → 23.10.1](https://github.com/psf/black/compare/23.10.0...23.10.1)

### Documentation
* docs: Add more badges ([`629857d`](https://github.com/sandialabs/reverse_argparse/commit/629857dc1c926be7cb0aa41b155be42d502822ef))

  Add additional badges to capture things like contributions, the
  conda-forge release channel, etc.
* docs: Include badges in ReadTheDocs ([`e30fc68`](https://github.com/sandialabs/reverse_argparse/commit/e30fc68c9d9ae8dc7a35b016b4024604e23ec5e5))

  Include the badges from the README in the index page of our
  documentation so this information is visible on ReadTheDocs in addition
  to GitHub and PyPI.

  Closes #81.
* docs: Private vulnerability reporting ([`9d6a758`](https://github.com/sandialabs/reverse_argparse/commit/9d6a758a95f47922f57eac814ba28e9046ee08e2))

  Remove the security issue template and instead direct people to file a
  private security advisory.

### Patch
* patch: Add a badge for the CodeQL action ([`2d77837`](https://github.com/sandialabs/reverse_argparse/commit/2d77837998ca69a46dd7579cbb89e9aa298b0ae4))

  Create a patch release to push all these new badges out to PyPI.

## v1.0.5 (2023-10-24)

### Chores
* chore: Update python-semantic-release config ([`9972341`](https://github.com/sandialabs/reverse_argparse/commit/997234115d3ad715ad2adb6b3a092193163a91f8))

  * Add commit types to automatically bump the minor or patch version
    numbers via a commit message.
  * Update commitizen configuration to allow the new commit types.
* chore: Add Python 3.12 to pyproject.toml ([`ef59c2d`](https://github.com/sandialabs/reverse_argparse/commit/ef59c2d76c9f51dcae6736dbe91436c647780245))

  This was accidentally omitted in
  6642a176e3591f3ef8ed0c04dbcbc4a257c5b127.
* chore: Remove YAPF configuration ([`ad02127`](https://github.com/sandialabs/reverse_argparse/commit/ad02127423354c1f42aff78728b9429c24647031))

  We switched to `black` back in #5.

### Continuous integration
* ci: pre-commit auto-update ([`cb014b7`](https://github.com/sandialabs/reverse_argparse/commit/cb014b7de64273369a4edb1df26ece2458f19850))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.10.1 → 3.12.0](https://github.com/commitizen-tools/commitizen/compare/3.10.1...3.12.0)
  - [github.com/pre-commit/mirrors-mypy: v1.6.0 → v1.6.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.6.0...v1.6.1)
  - [github.com/psf/black: 23.9.1 → 23.10.0](https://github.com/psf/black/compare/23.9.1...23.10.0)
  - [github.com/PyCQA/prospector: 1.10.2 → v1.10.3](https://github.com/PyCQA/prospector/compare/1.10.2...v1.10.3)
* ci: pre-commit auto-update ([`568c816`](https://github.com/sandialabs/reverse_argparse/commit/568c816514b50c014edf9cae79e1079055ccc437))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.10.0 → 3.10.1](https://github.com/commitizen-tools/commitizen/compare/3.10.0...3.10.1)
  - [github.com/pre-commit/mirrors-mypy: v1.5.1 → v1.6.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.5.1...v1.6.0)
* ci: pre-commit auto-update ([`b57dc9f`](https://github.com/sandialabs/reverse_argparse/commit/b57dc9f2f062679c453a97af3366dad7693bd2f2))

  updates:
  - [github.com/pre-commit/pre-commit-hooks: v4.4.0 → v4.5.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.4.0...v4.5.0)
* ci: Add Python 3.12 to CI ([`f03f4dc`](https://github.com/sandialabs/reverse_argparse/commit/f03f4dccde7188b8ea545d8bf3b626fefe652745))

  Also update the version badge to specify particular versions.
* ci: pre-commit auto-update ([`d9fc077`](https://github.com/sandialabs/reverse_argparse/commit/d9fc0777c37d1041610b8f775da7ee510e7b9111))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.9.0 → 3.10.0](https://github.com/commitizen-tools/commitizen/compare/3.9.0...3.10.0)
* ci: pre-commit auto-update ([`e97c276`](https://github.com/sandialabs/reverse_argparse/commit/e97c2768ffe210167bdd565e907cb4d418eaa2de))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.8.2 → 3.9.0](https://github.com/commitizen-tools/commitizen/compare/3.8.2...3.9.0)
* ci: pre-commit auto-update ([`87d1f7e`](https://github.com/sandialabs/reverse_argparse/commit/87d1f7e09ce5acc57ca58a455954b3273fc351ad))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.7.1 → 3.8.2](https://github.com/commitizen-tools/commitizen/compare/3.7.1...3.8.2)
  - [github.com/psf/black: 23.7.0 → 23.9.1](https://github.com/psf/black/compare/23.7.0...23.9.1)
* ci: pre-commit auto-update ([`b750046`](https://github.com/sandialabs/reverse_argparse/commit/b7500466de2d37dbb75df895a459749831a378c5))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.7.0 → 3.7.1](https://github.com/commitizen-tools/commitizen/compare/3.7.0...3.7.1)
* ci: pre-commit auto-update ([`b50b368`](https://github.com/sandialabs/reverse_argparse/commit/b50b368ea89d59fc8ba6f9ab1fac5971720af637))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.6.0 → 3.7.0](https://github.com/commitizen-tools/commitizen/compare/3.6.0...3.7.0)
* ci: pre-commit auto-update ([`989ba52`](https://github.com/sandialabs/reverse_argparse/commit/989ba523c4fe5bb93f0acc587f95805198352e7f))

  updates:
  - [github.com/pre-commit/mirrors-mypy: v1.5.0 → v1.5.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.5.0...v1.5.1)
* ci: Fix pre-commit auto-update message ([`6475b1f`](https://github.com/sandialabs/reverse_argparse/commit/6475b1f3ac2e5fff643a289859d452bbfa42099d))

  Ensure the commit message used by the pre-commit auto-update bot adheres
  to the Conventional Commits specification.
* ci: pre-commit autoupdate ([`08fe531`](https://github.com/sandialabs/reverse_argparse/commit/08fe531db0d29044440649a5fee7787ba691858c))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.5.3 → 3.6.0](https://github.com/commitizen-tools/commitizen/compare/3.5.3...3.6.0)
  - [github.com/pre-commit/mirrors-mypy: v1.4.1 → v1.5.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.4.1...v1.5.0)
  - [github.com/PyCQA/flake8: 6.0.0 → 6.1.0](https://github.com/PyCQA/flake8/compare/6.0.0...6.1.0)

### Documentation
* docs: Remove dependency pinning ([`b14034f`](https://github.com/sandialabs/reverse_argparse/commit/b14034fb44f39fec6e9db847053233bd10a24ccd))

  I should be the case that the bugs that kept us on an older version of
  Sphinx have been resolved at this point, so remove the version pinning.
* docs: Add sphinx-copybutton ([`2122825`](https://github.com/sandialabs/reverse_argparse/commit/2122825d7c31ebb91b7dd76af74c5cf61a4bd897))

  Automatically add a button to all code boxes to copy the contents to the
  clipboard.
* docs: Special thanks to @mjsumpter ([`6cc3054`](https://github.com/sandialabs/reverse_argparse/commit/6cc3054bd573da56c57505bcb11d057e38440dcb))

  Include @mjsumpter in the **Credits** section at the bottom of the
  README, as he put together a prior iteration of this concept under my
  guidance.  His earlier implementation informed the eventual creation of
  this package.
* docs: Fix typos ([`eb05c2c`](https://github.com/sandialabs/reverse_argparse/commit/eb05c2ca0b9bca8ada937d382d10185bc03e66e0))
* docs: Add CI details to contributing guidelines ([`b8269bf`](https://github.com/sandialabs/reverse_argparse/commit/b8269bf0c74a95bf65cddf1fb29eccf6db7b9cf8))
* docs: Check spelling ([`b72ee11`](https://github.com/sandialabs/reverse_argparse/commit/b72ee11874ae3b03280f623dbe08614aa023d689))

  Add sphinxcontrib-spelling extension to check the spelling in our
  documentation, and add a step to the CI job to ensure all is well.
* docs: Add OpenSSF Best Practices badge ([`604fb61`](https://github.com/sandialabs/reverse_argparse/commit/604fb6127229606c8e36dae4199b538e0ec12248))
* docs: Fix copy/paste issue ([`2f6517a`](https://github.com/sandialabs/reverse_argparse/commit/2f6517a9ad62412ea246d500170b0de7fe7e0e2f))
* docs: pre-commit install instructions ([`063d8f9`](https://github.com/sandialabs/reverse_argparse/commit/063d8f977d513f966d10889f7fc14386731a1c80))

### Patch
* patch: Add release notes template ([`a447eac`](https://github.com/sandialabs/reverse_argparse/commit/a447eac820ac9cadf081f1fdfeda1c4d5027552c))

  * Create a template to govern the generation of release notes by
    python-semantic-release.
  * Bump the patch version number to test that this works as expected.

### Testing
* test: Run examples in CI ([`6642a17`](https://github.com/sandialabs/reverse_argparse/commit/6642a176e3591f3ef8ed0c04dbcbc4a257c5b127))

  Create `example/test_examples.py` so `pytest` runs all the examples and
  checks their output.

## v1.0.4 (2023-07-25)

### Bug fixes
* fix: PyPI badge ([`1581e2a`](https://github.com/sandialabs/reverse_argparse/commit/1581e2a322caf39bd7a670c5c3f059713b4a43eb))

## v1.0.3 (2023-07-25)

### Bug fixes
* fix: Semantic release configuration ([`a73688c`](https://github.com/sandialabs/reverse_argparse/commit/a73688c434c203df0efde316bfdd5934a9ddee63))

## v1.0.2 (2023-07-24)

### Bug fixes
* fix: Release notes template ([`1ac839a`](https://github.com/sandialabs/reverse_argparse/commit/1ac839a5bf1a252830dd9bf9267bd049031b7f9b))
* fix: Semantic release configuration ([`0325dc0`](https://github.com/sandialabs/reverse_argparse/commit/0325dc0cd5dacee541f495652857fe43c9e1a3fe))

  * Add `__init__.py` to the files modified.
  * Fix the `__version__` in that file.
  * Remove trailing space in CHANGELOG template.
  * Add build command.
  * Make release commit match conventional standard.
  * Add release notes template.
  * Publish releases to PyPI and GitHub Releases.

### Continuous integration
* ci: Remove `-vv` for `semantic-release` ([`d83ae5d`](https://github.com/sandialabs/reverse_argparse/commit/d83ae5d1063a43de2822ba513b574745eed5a2e9))

## v1.0.1 (2023-07-20)

### Bug fixes
* fix: Include version in __init__.py ([`b7b369e`](https://github.com/sandialabs/reverse_argparse/commit/b7b369ec7ad3e8d58fbe0dd39b4acf2bc17bd568))

### Continuous integration
* ci: Rename workflow file ([`1cfed2d`](https://github.com/sandialabs/reverse_argparse/commit/1cfed2d0bd8833e633f684e717745ac65997d7ad))
* ci: Add conventional commits job ([`c683d7a`](https://github.com/sandialabs/reverse_argparse/commit/c683d7a9adf415f71816b190954cec4f4be3162d))
* ci: Set up semantice-release ([`9f233be`](https://github.com/sandialabs/reverse_argparse/commit/9f233bea255a44c5bb8470330c746ca6a951377e))

  Add a semantic-release configuration to `pyproject.toml`, with a custom
  `CHANGELOG.md` template.  Also add a GitHub Actions workflow.

### Documentation
* docs: Fix PyPI badge ([`edcc3d4`](https://github.com/sandialabs/reverse_argparse/commit/edcc3d4bb77a1b0c6a1ce22928e8a1965f015897))

### Unknown
* 1.0.1 ([`92bdc1a`](https://github.com/sandialabs/reverse_argparse/commit/92bdc1ade70d4b808f3be5a80e20ed6cb65517aa))

  Automatically generated by python-semantic-release.

## v1.0.0 (2023-07-18)

### Bug fixes
* fix: Move __init__.py ([`324f3e5`](https://github.com/sandialabs/reverse_argparse/commit/324f3e5b0dbb45144ca2b8afe258f8879b2fe6aa))

  Part of extracting this package from the repository it was initially
  developed in.
* fix: Correct method call ([`27fb201`](https://github.com/sandialabs/reverse_argparse/commit/27fb20153e46ad219a9f532f478f04391d3fb947))

  Should have been part of
  509fafb33329128ba8985578d66ab1bffe3fdbfb.
* fix: Omit suppressed arguments ([`9484360`](https://github.com/sandialabs/reverse_argparse/commit/948436060be2bfc53c6a1836b806d2c43438772a))

  If an argument's help text has been suppressed, and the value of the
  argument matches the default value, that indicated that a parser author
  has hidden an argument from users, and the user hasn't modified it on
  the command line.  To match the parser author's intent, such arguments
  should be omitted from the effective command line invocation.

### Chores
* chore: Enable Pyroma ([`124fa62`](https://github.com/sandialabs/reverse_argparse/commit/124fa629790976e0f5a0dcd3813d2aca34ad4cd1))
* chore: Enable Bandit ([`80e5bbe`](https://github.com/sandialabs/reverse_argparse/commit/80e5bbebf62361e54e53cfe41d55ee0e148ac4fb))
* chore: Add pre-commit hooks ([`1c2a015`](https://github.com/sandialabs/reverse_argparse/commit/1c2a01524adce4aecb55c7f6b636cdbe81c3e655))
* chore: Add pre-commit configuration ([`93ba0e7`](https://github.com/sandialabs/reverse_argparse/commit/93ba0e73b748a6b199d5f46f8b22873b6d39d14a))
* chore: Add VS Code settings ([`cc4edb2`](https://github.com/sandialabs/reverse_argparse/commit/cc4edb2611ed25a8a90751c03c8f69c8221db642))
* chore: Add __pycache__ to .gitignore ([`48a8acd`](https://github.com/sandialabs/reverse_argparse/commit/48a8acd77bad6b83a735b0540b5b184920715da9))

### Code style
* style: Address black issues ([`f2a8622`](https://github.com/sandialabs/reverse_argparse/commit/f2a86228680942d9b03d231e1d751c8e1aea2094))

### Continuous integration
* ci: Remove documentation jobs ([`81ab9c2`](https://github.com/sandialabs/reverse_argparse/commit/81ab9c230c3a19c8268b878c6e9364e3e1882266))

  Let ReadTheDocs test the PR instead.
* ci: Add Sphinx job to build the docs ([`671ac18`](https://github.com/sandialabs/reverse_argparse/commit/671ac18a9d6d83c3db4b1ccbe6fd0ca7b9180eb6))
* ci: Install all development dependencies ([`d8e7cf6`](https://github.com/sandialabs/reverse_argparse/commit/d8e7cf62f07157b8c6786755ed3818c371870526))
* ci: Switch to CodeCov ([`5899e2f`](https://github.com/sandialabs/reverse_argparse/commit/5899e2fcd3d1132097e05ff8e95f784d9b00cfd9))

  Abandon Coveralls, as it doesn't seem to integrate well with GitHub
  Actions.
* ci: Add Coveralls integration ([`7b19390`](https://github.com/sandialabs/reverse_argparse/commit/7b193900b0d1f20a24845b7a6ad02a784c0e8551))
* ci: Don't auto-fix PRs ([`cab73e9`](https://github.com/sandialabs/reverse_argparse/commit/cab73e90f4e41e24baae6a1634926e924fb4700c))
* ci: Switch flake8 ([`477646b`](https://github.com/sandialabs/reverse_argparse/commit/477646b2377bec35370e6f858e57bf2f0a03c5b5))

  Instead of running `flake8` in our GitHub Actions workflow, run it via
  pre-commit.ci.
* ci: Add initial workflow ([`9e42fcd`](https://github.com/sandialabs/reverse_argparse/commit/9e42fcdf0ccc5c7363528d110f0c7e331da30453))

  Create initial GitHub Actions workflow to lint and test the package.

### Documentation
* docs: Prepare for PyPI ([`511e859`](https://github.com/sandialabs/reverse_argparse/commit/511e85998ada5aae0bd61da7e127cfce81a28f51))
* docs: Fix punctuation. ([`cfc1279`](https://github.com/sandialabs/reverse_argparse/commit/cfc1279b9d614a601886042b905ec562d572f636))
* docs: Tweak badge ([`369b154`](https://github.com/sandialabs/reverse_argparse/commit/369b1542afd37b53ad0ea32275aa37174ca2e44d))
* docs: Sort badges in README ([`9db52fe`](https://github.com/sandialabs/reverse_argparse/commit/9db52fe8217eb3f09919b2898de6a816cebe0c62))
* docs: Add ReadTheDocs badge to README ([`df7e2db`](https://github.com/sandialabs/reverse_argparse/commit/df7e2dbd12a6dd1167448d8f035a503e633b849d))
* docs: Correct links ([`df1bde3`](https://github.com/sandialabs/reverse_argparse/commit/df1bde3befa88ecda2cbc9f76acca77c5a9099f0))

  Correct the URL for the documentation hosting on ReadTheDocs.
* docs: Create `_static` directory ([`6d83328`](https://github.com/sandialabs/reverse_argparse/commit/6d833282683190bce42932243f55fc6839e76a8f))
* docs: Install the package first ([`c00c692`](https://github.com/sandialabs/reverse_argparse/commit/c00c69288e8ef9b9ce49e3d72dbb9db2f7daf2a1))

  Try to `pip install .` as part of creating the environment for
  ReadTheDocs.
* docs: Add ReadTheDocs configuration ([`32e84f1`](https://github.com/sandialabs/reverse_argparse/commit/32e84f16820bb9bcc5ae0769104f408f1866a1ae))
* docs: Add Sphinx documentation ([`4595541`](https://github.com/sandialabs/reverse_argparse/commit/4595541e4f3fff5809147850294a881696716347))

  Create the Sphinx-based documentation for the package, including:

  * Getting started guidelines
  * The motivation for the package
  * Example use cases
  * Reference documentation for developers
* docs: Add CI badge to README ([`b14c7dd`](https://github.com/sandialabs/reverse_argparse/commit/b14c7ddd59bfb8f48f8ec0c81e294f7d8cf87a41))
* docs: Fix contributing guidelines ([`87afd52`](https://github.com/sandialabs/reverse_argparse/commit/87afd52e60b2416407d53c9a8373ec7eceee8381))
* docs: Address pydocstyle issues ([`1c1d2e2`](https://github.com/sandialabs/reverse_argparse/commit/1c1d2e2f50cdac418d46be231acaa6b5cf349484))
* docs: Update contributing guidelines ([`7f41b8d`](https://github.com/sandialabs/reverse_argparse/commit/7f41b8dd461d27a7d1bbe33718b6fa225117014b))

  Translate from GitLab to GitHub.
* docs: Add issue template ([`9e8cfc0`](https://github.com/sandialabs/reverse_argparse/commit/9e8cfc01d6132707ed30d707a78cecf8bb868384))
* docs: Update Markdown files ([`62c9115`](https://github.com/sandialabs/reverse_argparse/commit/62c9115ae7b2f3ecd888f15fdba165943710ec19))

  Tweaks to link syntax, etc.
* docs: Update README.md ([`1d69674`](https://github.com/sandialabs/reverse_argparse/commit/1d696743f2c8e4fe9c3858d97c5baffb33d04cf9))
* docs: Add LICENSE.md ([`72de284`](https://github.com/sandialabs/reverse_argparse/commit/72de2849d5a492a05d083e7f628ed434dd95e578))
* docs: Make unparse grammar consistent ([`bb55e4d`](https://github.com/sandialabs/reverse_argparse/commit/bb55e4d8d0e36e8376bac30f6b57e030800ac983))

  Make the spelling of unparse and its derivatives consistent (no
  hyphenation, not quoted) in all docstrings and text printed to the
  terminal.

### Features
* feat: Make private method public ([`509fafb`](https://github.com/sandialabs/reverse_argparse/commit/509fafb33329128ba8985578d66ab1bffe3fdbfb))

  Since classes/scripts using `reverse_argparse` may also need the ability
  to quote a command line argument if there are spaces in it, transition
  `quote_arg_if_necessary` from a private to a public method.  This will
  avoid code duplication outside `reverse_argparse`, and ensure classes
  and scripts that are using it are quoting arguments consistently.
* feat: Handle subparsers ([`b2262d5`](https://github.com/sandialabs/reverse_argparse/commit/b2262d561926f3aa75e70fa37e1bd6ad71c5b71a))

  Enable the unparsing of subparser actions by recursively pushing them
  onto the stack of parsers, unparsing them, and popping them back off the
  stack.

  Note:  This also makes it such that optional arguments are unparsed
  before positional ones, as this is required when dealing with
  subparsers.

### Refactoring
* refactor: Only support Python 3.8+ ([`8d15f4a`](https://github.com/sandialabs/reverse_argparse/commit/8d15f4ab124bb067f5422538050dd7c70b414aa8))

  Changes that can be undone when we remove 3.8 support:
  * Change certain type hints to work for 3.8
  * Use version guard around `BooleanOptionalAction`

  Changes that can be undone when we remove 3.9 support:
  * Switch match-case statement to if block.
* refactor: Address pylint issues ([`b4555dc`](https://github.com/sandialabs/reverse_argparse/commit/b4555dce7f91278145d2d1ee14bbdd25f8155e77))
* refactor: Address isort issues ([`fd6242d`](https://github.com/sandialabs/reverse_argparse/commit/fd6242dd5b25261aca064e5d380f4b930970ac60))
* refactor: Address mypy issues ([`403e53d`](https://github.com/sandialabs/reverse_argparse/commit/403e53da9d1b84e00f8814c90784dcae3f3158cb))
* refactor!: Build up `args` consecutively ([`d9a5639`](https://github.com/sandialabs/reverse_argparse/commit/d9a5639005824f0fdfb7e8570f2156179998cc71))

  Rework the class such that:

  * We initialize the `args` to a list of strings containing only the
    program name.
  * Each `_unparse_*` method appends a list of strings corresponding to
    the action to the `args`.
  * The `get_*_command_line_invocation` methods appropriately concatenate
    the elements in `args` into a single string.

  This sets us up for being able to handle sub-parser actions.

  Note that this is a breaking change, as it removes the `get_*_args`
  public methods.
* refactor: Display positional arguments first ([`ccf644d`](https://github.com/sandialabs/reverse_argparse/commit/ccf644daf915b86e82dae4637ed8ff75efbcbd9d))

  Display positional rather than optional arguments first in the effective
  command line.  This is necessary to prepare for the ability to handle
  sub-parsers.
* refactor: Prepare for nested parsers ([`ec3a7d8`](https://github.com/sandialabs/reverse_argparse/commit/ec3a7d832acc8903bf162792f62ab063175620a2))

  Change the `parser` attribute to be a list of parsers to prepare for
  processing nested parsers.

### Testing
* test: Adjust code coverage ([`b7aa09e`](https://github.com/sandialabs/reverse_argparse/commit/b7aa09ec6bd7d2ca09fec1bbce6914f9db5afdfc))
* test: Rework tests for calling program name ([`8c21452`](https://github.com/sandialabs/reverse_argparse/commit/8c21452ac0909536060828a6a3e3420a64244b01))

  As part of the transition from GitLab CI/CD to GitHub Actions, the
  program name used when running the tests has shifted from `__main__.py`
  to `pytest`.  This commits adjusts the tests to ignore the program name,
  and only pay attention to the arguments that come after it, such that
  the tests will work in both contexts.
* test: Fix import ([`65e57ba`](https://github.com/sandialabs/reverse_argparse/commit/65e57bad7a070bbbe7165caec709478d787b27f0))

  Rework how the tests import the class, given the package reorganization
  after pulling it out of the repository it was initially developed in.

### Unknown
* [pre-commit.ci] pre-commit autoupdate ([`a88839f`](https://github.com/sandialabs/reverse_argparse/commit/a88839f47b42d84cc24fda1ddf3501d7d9ed0628))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.5.2 → 3.5.3](https://github.com/commitizen-tools/commitizen/compare/3.5.2...3.5.3)
  - [github.com/psf/black: 23.3.0 → 23.7.0](https://github.com/psf/black/compare/23.3.0...23.7.0)
* [pre-commit.ci] pre-commit autoupdate ([`f0df3d3`](https://github.com/sandialabs/reverse_argparse/commit/f0df3d32a3d85429e9cc57ac55774292f9613e24))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.3.0 → 3.5.2](https://github.com/commitizen-tools/commitizen/compare/3.3.0...3.5.2)
  - [github.com/pre-commit/mirrors-mypy: v1.3.0 → v1.4.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.3.0...v1.4.1)
* [pre-commit.ci] pre-commit autoupdate ([`fd58d13`](https://github.com/sandialabs/reverse_argparse/commit/fd58d135f92fc227c37cdd908bf9acacaca246eb))

  updates:
  - [github.com/commitizen-tools/commitizen: 3.2.2 → 3.3.0](https://github.com/commitizen-tools/commitizen/compare/3.2.2...3.3.0)
* Add more issue templates ([`234b562`](https://github.com/sandialabs/reverse_argparse/commit/234b562299a42cb4eb1aa003b76a6fb9e8be3a2b))
* Add CHANGELOG.md ([`7bcc39d`](https://github.com/sandialabs/reverse_argparse/commit/7bcc39d3dc1691243f3af4bab16d9f188173b215))
* Add CONTRIBUTING.md ([`2b6dfc0`](https://github.com/sandialabs/reverse_argparse/commit/2b6dfc0b7c27666a672f370e978d8dae38395bd8))
* Add CODE_OF_CONDUCT.md ([`acbac7d`](https://github.com/sandialabs/reverse_argparse/commit/acbac7d6d40ec3771d6c009f0fc6488c2036a370))
* Add SECURITY.md ([`4ef978c`](https://github.com/sandialabs/reverse_argparse/commit/4ef978c7f221071d85e062fb16ce1430f696233a))
* Add README.md ([`4a0580c`](https://github.com/sandialabs/reverse_argparse/commit/4a0580cc0cbbdb7334a19d392ffd61cea252a3c5))
* Move __init__.py ([`c50bcd2`](https://github.com/sandialabs/reverse_argparse/commit/c50bcd27ad916376eb9d6fd11fa6236af69dca52))
* Add setup.py ([`1de083b`](https://github.com/sandialabs/reverse_argparse/commit/1de083b532f1aac92b692e304a0f3a4c579dd660))
* Add requirements.txt ([`75aa526`](https://github.com/sandialabs/reverse_argparse/commit/75aa52698241ff7ade31cfad6d3fc5269d24e92a))
* Add pyproject.toml ([`e833969`](https://github.com/sandialabs/reverse_argparse/commit/e8339695aee00086d0361475adc8b374106adcd8))
* Add .style.yapf ([`13d6301`](https://github.com/sandialabs/reverse_argparse/commit/13d63014fbbc999d1d11a235273f45c5b5ec9126))
* Add .gitignore ([`1c329cf`](https://github.com/sandialabs/reverse_argparse/commit/1c329cff71cc4c6e443539d3dcb3e65878af5530))
* Add .coveragerc ([`b43be41`](https://github.com/sandialabs/reverse_argparse/commit/b43be411421851129b3b022fbd79eb9a71a727cf))
* Unparse `BooleanOptionalAction` ([`cd82066`](https://github.com/sandialabs/reverse_argparse/commit/cd82066fbd080a48d8ae4e87d0ef23379234bbdd))
* Unparse `extend` action ([`3e9fbd3`](https://github.com/sandialabs/reverse_argparse/commit/3e9fbd380c5eade477d4cec2572397c451274cc7))
* Unparse `count` action ([`224b23b`](https://github.com/sandialabs/reverse_argparse/commit/224b23baa583d0581714906ef35d60fed5f8b724))
* Unparse `append_const` action ([`b22390a`](https://github.com/sandialabs/reverse_argparse/commit/b22390a3a854a92f31a14fd65a9844173c5dbb99))
* Unparse `store_const` action ([`64cc273`](https://github.com/sandialabs/reverse_argparse/commit/64cc2738ff6aceb66d814f588678c17b5085e46a))
* Create `reverse_argparse` module (#1873) ([`1ab310c`](https://github.com/sandialabs/reverse_argparse/commit/1ab310c697a31689dd52f97fcc26f05c00dcfb21))

  Create a module that is able to generate the effective command line
  invocation of a script, given the `ArgumentParser` that was used to
  parse the command line options, and the `Namespace` of those parsed
  options.  This makes it such that users can know exactly what was run,
  including all default values, and any transformations that might've been
  made to the arguments after parsing.

  This commit only implements the functionality we care about at the
  moment, which includes the following "actions":
  * store
  * store_true
  * store_false
  * append
  * help
  * version

  The remaining actions are stubbed out but not yet implemented:
  * store_const
  * append_const
  * count
  * extend
  * BooleanOptionalAction

  Also how sub-parsers are handled remains to be determined in the future.
