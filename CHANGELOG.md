# CHANGELOG



## v1.0.8 (2024-05-13)

### Chore
* chore: Remove commitizen configuration ([`73ceec1`](https://github.com/sandialabs/reverse_argparse/commit/73ceec1bdb5385744c29cef4eb85385603839ee7))
* chore: Remove commitizen pre-commit hook ([`18c274f`](https://github.com/sandialabs/reverse_argparse/commit/18c274f5b42764b8bca3527bd49841ae7bc920da))

  In order to enable a faster development workflow, remove the commitizen
  pre-commit hook to allow commits messages that don&#39;t adhere to the
  Conventional Commits specification.  Commit messages are still checked
  in the Continuous Integration workflow, though, so a branch will need to
  be clean before merging.

### Continuous Integration
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

### Test
* test: Ignore assert warnings in test files ([`01f97d0`](https://github.com/sandialabs/reverse_argparse/commit/01f97d037707378cf2fd7c86390c635dfbd5387b))

## v1.0.7 (2024-04-22)

### Chore
* chore: Ignore security findings in tests/examples ([`f18ece4`](https://github.com/sandialabs/reverse_argparse/commit/f18ece4a69291b96b84a80bd8eea0a5f51697026))
* chore: Switch to Ruff ([`6112943`](https://github.com/sandialabs/reverse_argparse/commit/6112943ca3f2a74c0419d8d2452884dd144c8309))

  Use Ruff to replace a variety of linters/formatters.
* chore: Fix badge URLs ([`2c8dda1`](https://github.com/sandialabs/reverse_argparse/commit/2c8dda1315e1d1297acea0f41a827736258d1950))

  Somehow it looks like some hidden character wound up copy/pasted in the
  middle of the `https`.
* chore: Add PR template ([`eb0b3b8`](https://github.com/sandialabs/reverse_argparse/commit/eb0b3b8da57b0c2a67b4928f4d3ae67890aa5bff))

### Continuous Integration
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
  &#34;private&#34; method, not in the package&#39;s public API.  Therefore the change
  is not registered as a breaking change via Conventional Commit syntax,
  and no major version update will be created.  Instead, this commit will
  force the creation of a patch release.  If users were relying on the
  prior behavior of this internal method, they can simply switch to the
  keyword syntax when calling it.

### Refactor
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
* refactor: Don&#39;t override Python builtins ([`9006adb`](https://github.com/sandialabs/reverse_argparse/commit/9006adbeefdbd08237325d91fbdf7ecf952b386d))

### Test
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

### Continuous Integration
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

### Chore
* chore: Update python-semantic-release config ([`9972341`](https://github.com/sandialabs/reverse_argparse/commit/997234115d3ad715ad2adb6b3a092193163a91f8))

  * Add commit types to automatically bump the minor or patch version
    numbers via a commit message.
  * Update commitizen configuration to allow the new commit types.
* chore: Add Python 3.12 to pyproject.toml ([`ef59c2d`](https://github.com/sandialabs/reverse_argparse/commit/ef59c2d76c9f51dcae6736dbe91436c647780245))

  This was accidentally omitted in
  6642a176e3591f3ef8ed0c04dbcbc4a257c5b127.
* chore: Remove YAPF configuration ([`ad02127`](https://github.com/sandialabs/reverse_argparse/commit/ad02127423354c1f42aff78728b9429c24647031))

  We switched to `black` back in #5.

### Continuous Integration
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
* docs: Fix typos ([`eb05c2c`](https://github.com/sandialabs/reverse_argparse/commit/eb05c2ca0b9bca8ada937d382d10185bc03e66e0))
* docs: Special thanks to @mjsumpter ([`6cc3054`](https://github.com/sandialabs/reverse_argparse/commit/6cc3054bd573da56c57505bcb11d057e38440dcb))

  Include @mjsumpter in the **Credits** section at the bottom of the
  README, as he put together a prior iteration of this concept under my
  guidance.  His earlier implementation informed the eventual creation of
  this package.
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

### Test
* test: Run examples in CI ([`6642a17`](https://github.com/sandialabs/reverse_argparse/commit/6642a176e3591f3ef8ed0c04dbcbc4a257c5b127))

  Create `example/test_examples.py` so `pytest` runs all the examples and
  checks their output.

## v1.0.4 (2023-07-25)

### Fix
* fix: PyPI badge ([`1581e2a`](https://github.com/sandialabs/reverse_argparse/commit/1581e2a322caf39bd7a670c5c3f059713b4a43eb))

## v1.0.3 (2023-07-25)

### Fix
* fix: Semantic release configuration ([`a73688c`](https://github.com/sandialabs/reverse_argparse/commit/a73688c434c203df0efde316bfdd5934a9ddee63))

## v1.0.2 (2023-07-24)

### Continuous Integration
* ci: Remove `-vv` for `semantic-release` ([`d83ae5d`](https://github.com/sandialabs/reverse_argparse/commit/d83ae5d1063a43de2822ba513b574745eed5a2e9))

### Fix
* fix: Release notes template ([`1ac839a`](https://github.com/sandialabs/reverse_argparse/commit/1ac839a5bf1a252830dd9bf9267bd049031b7f9b))
* fix: Semantic release configuration ([`0325dc0`](https://github.com/sandialabs/reverse_argparse/commit/0325dc0cd5dacee541f495652857fe43c9e1a3fe))

  * Add `__init__.py` to the files modified.
  * Fix the `__version__` in that file.
  * Remove trailing space in CHANGELOG template.
  * Add build command.
  * Make release commit match conventional standard.
  * Add release notes template.
  * Publish releases to PyPI and GitHub Releases.

## v1.0.1 (2023-07-20)

### Continuous Integration
* ci: Rename workflow file ([`1cfed2d`](https://github.com/sandialabs/reverse_argparse/commit/1cfed2d0bd8833e633f684e717745ac65997d7ad))
* ci: Add conventional commits job ([`c683d7a`](https://github.com/sandialabs/reverse_argparse/commit/c683d7a9adf415f71816b190954cec4f4be3162d))
* ci: Set up semantice-release ([`9f233be`](https://github.com/sandialabs/reverse_argparse/commit/9f233bea255a44c5bb8470330c746ca6a951377e))

  Add a semantic-release configuration to `pyproject.toml`, with a custom
  `CHANGELOG.md` template.  Also add a GitHub Actions workflow.

### Documentation
* docs: Fix PyPI badge ([`edcc3d4`](https://github.com/sandialabs/reverse_argparse/commit/edcc3d4bb77a1b0c6a1ce22928e8a1965f015897))

### Fix
* fix: Include version in __init__.py ([`b7b369e`](https://github.com/sandialabs/reverse_argparse/commit/b7b369ec7ad3e8d58fbe0dd39b4acf2bc17bd568))

### Unknown
* 1.0.1 ([`92bdc1a`](https://github.com/sandialabs/reverse_argparse/commit/92bdc1ade70d4b808f3be5a80e20ed6cb65517aa))

  Automatically generated by python-semantic-release.

## v1.0.0 (2023-07-18)

### Breaking
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

### Chore
* chore: Enable Pyroma ([`124fa62`](https://github.com/sandialabs/reverse_argparse/commit/124fa629790976e0f5a0dcd3813d2aca34ad4cd1))
* chore: Enable Bandit ([`80e5bbe`](https://github.com/sandialabs/reverse_argparse/commit/80e5bbebf62361e54e53cfe41d55ee0e148ac4fb))
* chore: Add pre-commit hooks ([`1c2a015`](https://github.com/sandialabs/reverse_argparse/commit/1c2a01524adce4aecb55c7f6b636cdbe81c3e655))
* chore: Add pre-commit configuration ([`93ba0e7`](https://github.com/sandialabs/reverse_argparse/commit/93ba0e73b748a6b199d5f46f8b22873b6d39d14a))
* chore: Add VS Code settings ([`cc4edb2`](https://github.com/sandialabs/reverse_argparse/commit/cc4edb2611ed25a8a90751c03c8f69c8221db642))
* chore: Add __pycache__ to .gitignore ([`48a8acd`](https://github.com/sandialabs/reverse_argparse/commit/48a8acd77bad6b83a735b0540b5b184920715da9))

### Continuous Integration
* ci: Remove documentation jobs ([`81ab9c2`](https://github.com/sandialabs/reverse_argparse/commit/81ab9c230c3a19c8268b878c6e9364e3e1882266))

  Let ReadTheDocs test the PR instead.
* ci: Add Sphinx job to build the docs ([`671ac18`](https://github.com/sandialabs/reverse_argparse/commit/671ac18a9d6d83c3db4b1ccbe6fd0ca7b9180eb6))
* ci: Install all development dependencies ([`d8e7cf6`](https://github.com/sandialabs/reverse_argparse/commit/d8e7cf62f07157b8c6786755ed3818c371870526))
* ci: Switch to CodeCov ([`5899e2f`](https://github.com/sandialabs/reverse_argparse/commit/5899e2fcd3d1132097e05ff8e95f784d9b00cfd9))

  Abandon Coveralls, as it doesn&#39;t seem to integrate well with GitHub
  Actions.
* ci: Add Coveralls integration ([`7b19390`](https://github.com/sandialabs/reverse_argparse/commit/7b193900b0d1f20a24845b7a6ad02a784c0e8551))
* ci: Don&#39;t auto-fix PRs ([`cab73e9`](https://github.com/sandialabs/reverse_argparse/commit/cab73e90f4e41e24baae6a1634926e924fb4700c))
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

### Feature
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

### Fix
* fix: Move __init__.py ([`324f3e5`](https://github.com/sandialabs/reverse_argparse/commit/324f3e5b0dbb45144ca2b8afe258f8879b2fe6aa))

  Part of extracting this package from the repository it was initially
  developed in.
* fix: Correct method call ([`27fb201`](https://github.com/sandialabs/reverse_argparse/commit/27fb20153e46ad219a9f532f478f04391d3fb947))

  Should have been part of
  509fafb33329128ba8985578d66ab1bffe3fdbfb.
* fix: Omit suppressed arguments ([`9484360`](https://github.com/sandialabs/reverse_argparse/commit/948436060be2bfc53c6a1836b806d2c43438772a))

  If an argument&#39;s help text has been suppressed, and the value of the
  argument matches the default value, that indicated that a parser author
  has hidden an argument from users, and the user hasn&#39;t modified it on
  the command line.  To match the parser author&#39;s intent, such arguments
  should be omitted from the effective command line invocation.

### Refactor
* refactor: Only support Python 3.8+ ([`8d15f4a`](https://github.com/sandialabs/reverse_argparse/commit/8d15f4ab124bb067f5422538050dd7c70b414aa8))

  Changes that can be undone when we remove 3.8 support:
  * Change certain type hints to work for 3.8
  * Use version guard around `BooleanOptionalAction`

  Changes that can be undone when we remove 3.9 support:
  * Switch match-case statement to if block.
* refactor: Address pylint issues ([`b4555dc`](https://github.com/sandialabs/reverse_argparse/commit/b4555dce7f91278145d2d1ee14bbdd25f8155e77))
* refactor: Address isort issues ([`fd6242d`](https://github.com/sandialabs/reverse_argparse/commit/fd6242dd5b25261aca064e5d380f4b930970ac60))
* refactor: Address mypy issues ([`403e53d`](https://github.com/sandialabs/reverse_argparse/commit/403e53da9d1b84e00f8814c90784dcae3f3158cb))
* refactor: Display positional arguments first ([`ccf644d`](https://github.com/sandialabs/reverse_argparse/commit/ccf644daf915b86e82dae4637ed8ff75efbcbd9d))

  Display positional rather than optional arguments first in the effective
  command line.  This is necessary to prepare for the ability to handle
  sub-parsers.
* refactor: Prepare for nested parsers ([`ec3a7d8`](https://github.com/sandialabs/reverse_argparse/commit/ec3a7d832acc8903bf162792f62ab063175620a2))

  Change the `parser` attribute to be a list of parsers to prepare for
  processing nested parsers.

### Style
* style: Address black issues ([`f2a8622`](https://github.com/sandialabs/reverse_argparse/commit/f2a86228680942d9b03d231e1d751c8e1aea2094))

### Test
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
  including all default values, and any transformations that might&#39;ve been
  made to the arguments after parsing.

  This commit only implements the functionality we care about at the
  moment, which includes the following &#34;actions&#34;:
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
