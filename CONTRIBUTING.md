# Contributing to reverse_argparse

Thanks so much for your willingness to help out with `reverse_argparse`'s
development :grinning:  Here's everything you need to know.



## Contributor License Agreement

By contributing to this software project, you are agreeing to the following
terms and conditions for your contributions:

* You agree your contributions are submitted under the
  [license used by this project](LICENSE.md).
* You represent you are authorized to make the contributions and grant the
  license.  If your employer has rights to intellectual property that includes
  your contributions, you represent that you have received permission to make
  contributions and grant the required license on behalf of that employer.



## Setting Up Your Environment

Before you begin hacking on `reverse_argparse`, you'll need to do four things:

1. **Fork the Repository:**  On [`reverse_argparse`'s main page][homepage], in
   the top-right corner, you'll see a button to [fork the repository][fork].
   Do so, and then clone your fork and set it up with
   ```bash
   git clone git@github.com:${USER}/reverse_argparse
   cd reverse_argparse
   git remote add upstream git@github.com:sandialabs/reverse_argparse
   git fetch upstream
   ```
2. **Set Up your Environment:**  Install the requirements with
   ```bash
   cd /path/to/reverse_argparse
   python3 -m pip install \
     -r requirements.txt \
     -r doc/requirements.txt \
     -r example/requirements.txt \
     -r test/requirements.txt
   ```
3. **Run the Examples:**  Ensure you can run all the examples with
   ```bash
   cd /path/to/reverse_argparse/example
   ./run-all.bash
   ```
4. **Build the Documentation:**  Ensure you can build the documentation with
   ```bash
   cd /path/to/reverse_argparse/doc
   ./make-html.bash
   ```

[homepage]: https://github.com/sandialabs/reverse_argparse
[fork]: https://docs.github.com/en/get-started/quickstart/fork-a-repo

### Pre-Commit

We use [pre-commit][precommit] to ensure adherence to Python best practices,
enforce our style guide, etc.  To set yourself up with it, ensure you have your
development environment activated, and then run
```bash
cd /path/to/reverse_argparse
pre-commit install
pre-commit install --hook-type commit-msg --hook-type pre-push
```

[precommit]: https://pre-commit.com/

The checks we perform are the following:
* Use [ruff][ruff] to lint and format the code and docstrings.
* Use [mypy][mypy] to run static type checking on our type-hinted code.
* Ensure no large files are added to the repository.
* Ensure files parse as valid Python.
* Check for files that would conflict in case-sensitive filesystems.
* Ensure files don't contain merge conflict strings.
* Ensure files end with a single blank line.
* Ensure we only use Unix line endings.
* Trim trailing whitespace.
* Ensure we use [type-hinting][typing].
* Check for common mistakes in [reStructuredText][rest] in our documentation.
* Use [doc8][doc8] to enforce our style for our documentation.
* Use [pyroma][pyroma] to ensure our package complies with the best practices
  of the Python packaging ecosystem.

[ruff]: https://docs.astral.sh/ruff/
[mypy]: https://github.com/python/mypy
[typing]: https://docs.python.org/3/library/typing.html
[rest]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
[doc8]: https://github.com/PyCQA/doc8
[pyroma]: https://github.com/regebro/pyroma

### VS Code

Our IDE of choice is [VS Code][vscode].  Download and install it, and then
follow the instructions below to get it set up.

[vscode]: https://code.visualstudio.com/

#### Getting Started

For getting up and running with VS Code, check out the following resources:

* [Visual Studio Code:  Introductory Videos][videos]
* [Visual Studio Code:  Getting Started][gettingstarted] documentation
* [Python Development in Visual Studio Code][pyvscode] from
  [RealPython.com][realpython]
* [Advanced Visual Studio Code for Python Developers][advanced] from
  [RealPython.com][realpython]
* One-page reference of keyboard shortcuts for [Linux][linux], [MacOS][mac],
  and [Windows][win]

[videos]: https://code.visualstudio.com/docs/getstarted/introvideos
[gettingstarted]: https://code.visualstudio.com/docs
[pyvscode]: https://realpython.com/python-development-visual-studio-code/
[realpython]: http://realpython.com/
[advanced]: https://realpython.com/advanced-visual-studio-code-python/
[linux]: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf
[mac]: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf
[win]: https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf

#### Extensions

VS Code is highly customizable through the use of extensions.  Click on the
building blocks icon on the left-hand side to open the **EXTENSIONS** panel to
search for and install them.  These are the ones we recommend:

**General**
* **Better Comments:**  Style comments in a more human-friendly manner.
* **Code Spell Checker:**  Catch spelling mistakes in code and comments.
* **Conventional Commits:**  Adhere to the [Conventional Commits][conventional]
  specification for commit messages.
* **Coverage Gutters:**  Display test coverage in the editor.
* **GitLens — Git supercharged:**  Integrate some of the powerful features of
  [GitKraken][kraken] into VS Code.
* **IntelliCode:**  AI-assisted development features.
* **Pre-Commit:**  Commands and helpers for executing pre-commit hooks.
* **Test Adapter Converter:**  Converts from the Test Explorer UI (below) API
  to native VS Code testing.
* **Test Explorer UI:**  Extensible user interface for running your tests in VS
  Code.
* **Vim:**  For when you can't truly leave vi behind (and who would want to?).
* **vscode-icons:**  Icons for the file explorer.

[conventional]: https://www.conventionalcommits.org/en/v1.0.0/
[kraken]: https://www.gitkraken.com/

**Python-Specific**
* **AREPL for python:**  Automatically evaluate Python code as you type in the
  editor.
* **autoDocstring - Python Docstring Generator:**  Quickly generate docstrings
  for Python functions.
* **Mpy Type Checker:**  Type checking support for Python.
* **Pylance:**  Fast, feature-rich language support for Python.
* **Pytest IntelliSense:**  Adds IntelliSense support for [pytest][pytest]
  fixtures.
* **Python:**  Rich support for the Python language.
* **Python Indent:**  Correct Python indentation.
* **Python Test Explorer:**  Run your [unittest][unittest], [pytest][pytest],
  or [testplan][testplan] tests with the Test Explorer UI (see **General**
  above).
* **Python Type Hint:**  Type hint autocompletion.
* **Ruff:**  Automatic linting and formatting.
* **Sourcery:**  Automatic code review and refactoring.

[unittest]: https://docs.python.org/3/library/unittest.html
[testplan]: https://github.com/morganstanley/testplan

#### Settings

After installing the various extensions, you'll also want to customize your
**Settings**.  Some things can be set in the [Settings editor][settings]:

[settings]: https://code.visualstudio.com/docs/getstarted/settings#_settings-editor

* Text Editor
  * Font
    * **Font Family:**  Add "'Hack FC Ligatured', " to the beginning of the
      list.  You'll also want to install the [Ligatured Hack fonts][hack] on
      your system.
  * Files
    * **Auto Save:**  Set to "onFocusChange".
    * **Trim Trailing Whitespace:**  Check.
* Extensions
  * Conventional Commits
    * **Show Editor:**  Check.
    * **Silent Auto Commit:**  Check.
  * coverage-gutters
    * **Coverage-gutters: Show Line Coverage:**  Check.
    * **Coverage-gutters: Show Ruler Coverage:**  Check.
  * Git
    * **Allow Force Push:**  Check.
    * **Autofetch:**  Set to "true".
    * **Enable Smart Commit:**  Check.
    * **Fetch On Pull:**  Check.
    * **Prune On Fetch:**  Check.
    * **Rebase When Sync:**  Check.  This makes it such that you use `git pull
      --rebase` when pulling.
    * **Show Push Success Notification:**  Check.
    * **Terminal Git Editor:**  Check.
  * pre-commit-helper
    * **Run On Save:**  Select "all hooks".
  * Python Docstring Generator configuration
    * **Docstring Format:**  Select "google-notypes".
    * **Start On New Line:**  Check.
  * Sourcery Configuration:
    * **Token:**  [Create a free Sourcery account][sourcery], generate a token,
      and paste it here.
  * Vim
    * **Vimrc:**  Enable:  Check.

[hack]: https://github.com/gaplo917/Ligatured-Hack
[sourcery]: https://sourcery.ai/

Other items can be customized in the [`settings.json` file][settingsjson].
Consider adding the following snippets:

[settingsjson]: https://code.visualstudio.com/docs/getstarted/settings#_settingsjson

* To use ligatures to make multi-character symbols in code more readable, add
  ```json
  "editor.fontLigatures": true,
  ```
* To add vertical rulers to the editor window, add
  ```json
  "editor.rulers": [
      72,
      79
  ],
  ```
  The line at 79 characters is to remind you of the maximum line length, and
  the one at 72 characters is to remind you of the maximum line length for
  comments and docstrings (see [PEP8][pep8]).
* If you'd like the UI to preserve the scope that you're currently editing at
  the top of the file as you scroll through it, you can add
  ```json
  "editor.experimental.stickyScroll.enabled": true,
  ```
* To turn on search highlighting when using the Vim extension, add
  ```json
  "vim.hlsearch": true,
  ```
* To set up `pytest`, such that it produces coverage information, add
  ```json
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
      "-v",
      "--cov",
      "--cov-report=html",
      "--cov-report=json",
      "--cov-report=xml",
      "."
  ],
  ```

[pep8]: https://peps.python.org/pep-0008/#maximum-line-length

A final setting needs to be configured in the [`launch.json` file][launchjson].
You'll need to add the following to the list of configurations:
```json
"configurations": [
    {
        ... # Existing configuration.
    },
    {
        "name": "Python: Debug Tests",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "purpose": ["debug-test"],
        "console": "integratedTerminal",
        "env": {
            "PYTEST_ADDOPTS": "--no-cov"
        },
        "justMyCode": false
    }
]
```
This will make it such that when debugging unit testing, the debugger doesn't
restrict itself to only your code.

[launchjson]: https://code.visualstudio.com/docs/editor/debugging#_launch-configurations

#### Choosing a Python Interpreter

Once you've taken care of all the settings above, you're almost ready to start
Python development with VS Code.  Before you do, though, you'll need to select
your Python interpreter.  Open the command palette, start typing "python
interpreter," and select **Python: Select Interpreter**.  It will pop up a list
of Python installations it could find on your system.  Pick the one that
corresponds to your development environment (see
[above](#setting-up-your-environment)).

#### Setting Up PyTest

The last step in setting up VS Code for Python development is to ensure
`pytest` is working.  Click on the flask icon on the left-hand side to open the
**TESTING** panel on the left.  There will be two collapsible sections labeled
**TEST EXPLORER**.  Collapse the top one (it comes from an extension that
doesn't quite work for Python testing), and expand the bottom one.  You should
be able to hover over a test file, click the play button, and see the tests
pass.  If so, go ahead and click the three dots at the top-right of the
**TESTING** panel and deselect the top **Test Explorer**.

Running your test suite will generate code coverage information, which you can
then view in the editor.  After you've run your tests, open up one of your code
files, open the command palette, type "coverage," and select
**Coverage-Gutters: Toggle Coverage**.  This will highlight covered and
uncovered lines in green and red, respectively.  You can also view the full
coverage report by opening `test/htmlcov/index.html`.



## Coding Standards

Many of our coding standards are applied and enforced using
[pre-commit][precommit] (see [above](#pre-commit)).  In addition to what's
handled automatically, we have the following.

### Documentation

Classes and functions should be documented with [docstrings][docstrings] using
the [Google-style][google] format.  The contents of docstrings should use
[reStructuredText][rest] formatting.  This is so we can use [Sphinx][sphinx] to
generate [our documentation][docs].  Additionally, function definitions should
utilize [type-hinting][typing] wherever possible for clarity's sake.

[docstrings]: https://www.python.org/dev/peps/pep-0257
[google]: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
[docs]: https://reverse-argparse.readthedocs.io
[sphinx]: https://www.sphinx-doc.org/en/master/

### Testing

We use [pytest][pytest] for our unit test suite.  To get up-to-speed with what
it does and how it works, check out [this RealPython tutorial][tutorial].  Also
highly recommended is [Python Testing with pytest, by Brian Okken][okken].

[pytest]: https://docs.pytest.org/
[tutorial]: https://realpython.com/pytest-python-testing/
[okken]: https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409/ref=sr_1_2?keywords=pytest&qid=1637712723&sr=8-2

Please add tests to cover any new functions you create, and adhere to the
following guidelines:
* Each module (`module_name.py`) should have a corresponding test file
  (`test_module_name.py`).
* Each function/method in a module should have at least one corresponding test.
* The test order should match the ordering of the functions/methods being
  tested in the module, such that users can easily scroll through the two files
  side-by-side.
* Prefer parametrizing a test function over creating a separate test function.
* But don't go too crazy with that&mdash;use your judgment.
* Place any fixture definitions at the top of the test file.

### Best Practices

* Docstrings and comments should be grammatically correct English
  (capitalization, punctuation, full sentences, etc.).
* Prefer double quotes over single quotes.
* Use `pathlib.Path` and associated methods to represent all path-like objects.
* Use [f-strings][fstrings] for formatting strings.
* Alphabetize class attributes in the docstring and `__init__()` to ease
  readability/maintainability/extensibility.
* Prefer alphabetizing keyword arguments to functions, unless a different
  ordering would be more logical in a specific situation.
* Blank lines in functions should be avoided unless preceding a comment
  indicating a section of code.  However, if your function is broken up into
  sections via comments, consider subdividing it into smaller functions.
* Prefer imports of the form
  ```python
  from package import Class
  ```
  as opposed to
  ```python
  import package
  ```
  if only using a small handful of things from the package.

[fstrings]: https://peps.python.org/pep-0498/



## Creating Issues

Create [issues][issues] in GitHub for any work that needs to be done.

[issues]: https://github.com/sandialabs/reverse_argparse/issues

### Markdown

[Markdown][markdown] is a lightweight markup language with plain text
formatting syntax.  GitHub uses a form of it for rendering issue and pull
request descriptions and comments, wiki pages, and any files in your
repositories with a `.md` extension (such as this one).  For more details on
what's possible with GitHub-flavored Markdown, [see the documentation][gfm].

[markdown]: https://en.wikipedia.org/wiki/Markdown
[gfm]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

### Issue Templates

When creating an issue, select one of the available issue templates, and then
follow the instructions that appear in the template.

### Labels

The [reverse_argparse > Labels][labels] page shows you all the labels we use,
along with their descriptions.  "Type" labels will be applied automatically
when an issue is created via the issue template.  "Stage" labels are used to
keep track of what work is being done at any given time.  Other labels can be
added as appropriate.

[labels]: https://github.com/sandialabs/reverse_argparse/labels



## Working Issues

### Planning Work

Depending on the needs of the `reverse_argparse` user base, a project
maintainer will schedule issues to be tackled in the near future by applying
the "Stage:  Soon" label.  An issue can then be grabbed by a member of the
development team when they have some time available to work on it.

> **Note:**  If you're working on something that hasn't been
> scheduled&mdash;e.g., you're tackling a quick bug fix, or are tinkering with
> a feature you'd like to see added&mdash;don't worry about the "Stage:  Soon"
> label; just work on it as per the rest of the guidelines below.

### When Work Begins

First switch the label from "Stage:  Soon" to "Stage:  Development".  Next make
sure your local `master` branch is up-to-date with
```bash
git checkout master
git pull --ff-only upstream master
```

> **Note:**  You should never be making commits on your `master` branch.  The
> `--ff-only` ensures you only update your local `master` branch if it can be
> fast-forwarded.

Once `master` is updated, you then create a feature branch off of it with
```bash
git checkout -b <branch-name>
```

The recommended branch naming convention is to use the issue number, followed
by a hyphen, followed by the issue title, all lowercase, omitting special
characters, and replacing spaces with hyphens.  For instance, if issue number
123 has "Implement Awesome New Feature" as the title, the corresponding branch
name would be `123-implement-awesome-new-feature`.

### As Work Continues

Do whatever work is necessary to address the issue you're tackling.  Break your
work into logical, working commits.  Use the **Conventional Commits** extension
for VS Code (or something similar) to ensure your commit messages adhere to the
[Conventional Commits specification][conventional].

Feel free to commit and push small chunks early and often and then use
interactive rebase to reorganize your commits before sharing.

> **Note:**  If you rebase a branch that's already been pushed to a remote,
> you'll wind up changing the history, which will require a force push.  That
> is permissible (even encouraged), but if you've had one or more reviewers or
> collaborators working with you on the branch, *get their buy-in first* before
> doing a force push.

### When Work is Complete

While working on your feature in your local `<branch-name>` branch, other
commits will likely make it into the upstream `master` branch.  There are a
variety of ways to merge these changes into your local feature branch.  One
possibility is
```bash
git checkout master
git pull --ff-only upstream master
git checkout <branch-name>
git rebase master
```

though there are others that are equally valid.  Once all is well, create a
pull request (see below).

### Closing Old Issues

If at any point you encounter an issue that will not be worked in the
foreseeable future, it is worthwhile to close the issue such that we can
maintain a reasonable backlog of upcoming work.  Do be sure to include in the
comments some explanation as to why the issue won't be addressed.



## Pull Requests

The only way changes get into `master` is through pull requests.  When you've
completed work on an issue, push your branch to your fork with `git push -u
origin <branch-name>`, and then create a pull request.  Apply the same "Type"
label as the issue, and then return to the issue and swap "Stage:  Development"
for "Stage:  Review".

### Reviews

A project maintainer will review your pull request.  Work with them to get your
changes into an acceptable state.

### Drafts

You may wish to have your changes reviewed by colleagues before they are ready
to be merged into `master`.  To do so, create a [draft pull request][drafts].
GitHub will not allow you to merge a draft request.  When it's ready for
review, you can [mark it as ready][ready].

[drafts]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests
[ready]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review

### Continuous Integration

GitHub Actions is GitHub's continuous integration and delivery (CI/CD)
mechanism.  The configurations for our workflows can be found in the `*.yml`
files in [the `.github/workflows` directory](.github/workflows) in the
repository root:
* **Continuous Integration:**  This workflow runs a `test` job, parametrized
  across the currently maintained versions of Python, to ensure unit testing
  passes, and a `commits` job to ensure we're adhering to the [Conventional
  Commits specification][conventional].
* **Semantic Release:**  This workflow runs on merges to `master` to
  automatically generate and publish new releases, based on the commits just
  merged.

In addition to the GitHub Actions workflows, we also integrate with the
following services:
* [Codecov][codecov]:  We calculate and publish code coverage details for all
  PRs and merged into `master`, and the service comments on PRs indicating any
  changes in coverage compared to the base branch.
* [ReadTheDocs][readthedocs]:  We ensure our documentation builds for all PRs,
  and the documentation is published for `master` and all release tags.
* [pre-commit.ci][precommitci]: We ensure all the `pre-commit` checks we
  encourage developers to run locally also run in CI.

[codecov]: https://about.codecov.io/
[readthedocs]: https://about.readthedocs.com/?ref=readthedocs.org
[precommitci]: https://pre-commit.ci/

### Merging

When the review is finished and changes are ready to be merged into `master`:
1. Rebase your feature branch on top of the latest `master`.
2. Clean up your branch with an interactive rebase, squashing down to the
   smallest number of commits that makes sense.  If there are successive
   distinct changes in a pull request, it's fine for those to be preserved in
   separate commits.
3. Notify your reviewers that the request is ready to merge.
4. Wait for them to merge the request.
5. Ensure the post-merge CI pipeline also succeeds.



## Conventional Comments

When commenting on issues and pull requests, we endeavor to adhere to the
[Conventional Comments specification][conventionalcomments] wherever
applicable.  Comments should have the form
```
<label> [decorations]: <subject>

[discussion]
```
where:
* **label:**  This is a single label that signifies what kind of comment is
  being left.
* **subject:**  This is the main message of the comment.
* **decorations (optional):**  These are extra decorating labels for the
  comment.  They are surrounded by parentheses and comma-separated.
* **discussion (optional):**  This contains supporting statements, context,
  reasoning, and anything else to help communicate the “why” and “next steps”
  for resolving the comment.

The labels we use are the following:

* **chore:**  Chores are simple tasks that must be done before the subject can
  be “officially” accepted.  Usually, these comments reference some common
  process.  Try to leave a link to the process description so that the reader
  knows how to resolve the chore.
* **issue:**  Issues highlight specific problems with the subject under review.
  These problems can be user-facing or behind the scenes.  It is strongly
  recommended to pair this comment with a suggestion.  If you are not sure if a
  problem exists or not, consider leaving a **question**.
* **note:**  Notes are always non-blocking and simply highlight something the
  reader should take note of.
* **polish:**  Polish comments are like a suggestion, where there is nothing
  necessarily wrong with the relevant content, there's just some ways to
  immediately improve the quality.
* **praise:**  Praises highlight something positive.  Try to leave at least one
  of these comments per review.  Do not leave false praise (which can actually
  be damaging).  Do look for something to sincerely praise.
* **quibble:**  Quibbles are trivial, preference-based requests.  These should
  be non-blocking by nature.
* **suggestion:**  Suggestions propose improvements to the current subject.
  It's important to be explicit and clear on what is being suggested and why it
  is an improvement.  Consider using patches and the blocking or non-blocking
  decorations to further communicate your intent.
* **thought:**  Thoughts represent an idea that popped up from reviewing.
  These comments are non-blocking by nature, but they are extremely valuable
  and can lead to more focused initiatives and mentoring opportunities.
* **todo:**  TODO's are small, trivial, but necessary changes.  Distinguishing
  **todo** comments from **issues** or **suggestions** helps direct the
  reader's attention to comments requiring more involvement.
* **typo:**  Typo comments are like **todo**, where the main issue is a
  misspelling.
* **question:**  Questions are appropriate if you have a potential concern but
  are not quite sure if it's relevant or not.  Asking the author for
  clarification or investigation can lead to a quick resolution.

The decorations we use are the following:

* **if-minor:**  This decoration gives some freedom to the author that they
  should resolve the comment only if the changes ends up being minor or
  trivial.
* **non-blocking:**  A comment with this decoration should not prevent the
  subject under review from being accepted.  Without this decoration, comments
  are assumed to be blocking.

[conventionalcomments]: https://conventionalcomments.org/
