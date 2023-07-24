# CHANGELOG




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
