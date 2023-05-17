# Contributing to reverse_argparse

Thanks so much for your willingness to help out with `reverse_argparse`'s
development :grinning:  Here's everything you need to know.

<details>
<summary><b>Contents</b></summary>
<ul>
  <li><a href="#getting-started">Getting Started</a></li>
  <li>
    <a href="#creating-issues">Creating Issues</a>
    <ul>
      <li><a href="#markdown">Markdown</a></li>
      <li><a href="#issue-templates">Issue Templates</a></li>
      <li><a href="#labels">Labels</a></li>
    </ul>
  </li>
  <li>
    <a href="#working-issues">Working Issues</a>
    <ul>
      <li><a href="#planning-work">Planning Work</a></li>
      <li><a href="#when-work-begins">When Work Begins</a></li>
      <li>
        <a href="#as-work-continues">As Work Continues</a>
        <ul>
          <li><a href="#commit-messages">Commit Messages</a></li>
          <li><a href="#pytest">pytest</a></li>
          <li><a href="#sphinx">Sphinx</a></li>
        </ul>
      </li>
      <li><a href="#when-work-is-complete">When Work is Complete</a></li>
      <li><a href="#closing-old-issues">Closing Old Issues</a></li>
    </ul>
  </li>
  <li>
    <a href="#pull-requests">Pull Requests</a>
    <ul>
      <li><a href="#reviewers">Reviewers</a></li>
      <li><a href="#drafts">Drafts</a></li>
      <li><a href="#gitlab-ci">GitHub CI</a></li>
      <li><a href="#merging">Merging</a></li>
    </ul>
  </li>
</ul>
</details>



## Getting Started

Before you begin hacking on `reverse_argparse`, you'll need to do two things:

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
     -r test/requirements.txt \
     -r doc/requirements.txt
   ```

   Make sure you can run the test suite with
   ```bash
   python3 -m pytest test/
   ```

   and that you can build the documentation with
   ```bash
   cd doc
   bash make_html_docs.sh
   ```

If you're able to do all the above successfully, then you're ready to start
work.

[homepage]: https://github.com/sandialabs/reverse_argparse
[fork]: https://docs.github.com/en/get-started/quickstart/fork-a-repo



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

The recommended branch naming convention is to use the issue number, following
by a hyphen, followed by the issue title, all lowercase, omitting special
characters, and replacing spaces with hyphens.  For instance, if issue number
123 has "Implement Awesome New Feature" as the title, the corresponding branch
name would be `123-implement-awesome-new-feature`.

### As Work Continues

Do whatever work is necessary to address the issue you're tackling.  Break your
work into logical, working commits.  Use either the
[Conventional Commit plugin for Pycharm][jetbrains] or the
[Conventional Commits extension for VS Code][vscode] (or something similar) to
ensure your commit messages adhere to the
[Conventional Commits specification][conventionalcommits].

[jetbrains]: https://plugins.jetbrains.com/plugin/13389-conventional-commit
[vscode]: https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits
[conventionalcommits]: https://www.conventionalcommits.org/en/v1.0.0/

Feel free to commit and push small chunks early and often and then use `git
rebase -i` to reorganize your commits before sharing.

> **Note:**  If you rebase a branch that's already been pushed to a remote,
> you'll wind up changing the history, which will require a force push with
> `git push origin +<branchName>`.  That is permissible (even encouraged), but
> if you've had one or more reviewers or collaborators working with you on the
> branch, *get their buy-in first* before doing a force push.

#### Commit Messages

Make sure your commit messages reference the appropriate issue numbers using
the `#<issueNumber>` syntax.  The first line of the commit message should be a
descriptive title, limited to 50 characters.  This is then followed by a blank
line, and then the rest of the commit message is a description of the changes,
particularly *why* they were made, limited to 72 characters wide.

#### pytest

`reverse_argparse` uses [`pytest`][pytest] for our unit test suite.  Please add
tests to cover any new functions you create.

[pytest]: https://docs.pytest.org/

#### Sphinx

`reverse_argparse` uses [Sphinx][sphinx] to generate [our documentation][docs].
You'll want to be familiar with the [Google docstring format][googledocstring]
and [reStructuredText][restructuredtext] for the sake of updating our
documentation while changing the code itself.

[sphinx]: https://www.sphinx-doc.org/en/master/
[docs]: https://reverse_argparse.readthedocs.io
[googledocstring]: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
[restructuredtext]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

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

### Reviewers

A project maintainer will review your pull request.  Work with them to get your
changes into an acceptable state.

### Drafts

You may wish to have your changes reviewed by colleagues before they are ready
to be merged into `master`.  To do so, create a [draft pull request][drafts].
GitHub will not allow you to merge a draft request.  When it's ready for
review, you can [mark it as ready][ready].

[drafts]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests
[ready]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review

### GitHub CI

> **NOTE:**  REWORK THIS SECTION WHEN CI IS SET UP.

GitHub CI will automatically run on your pull request.  The configuration for
the pipeline can be found in [the `.gitlab-ci.yml` file](INSERT URL HERE) in
the repository root.

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
