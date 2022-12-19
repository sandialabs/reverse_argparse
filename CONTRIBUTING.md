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
      <li><a href="#linked-issues">Linked Issues</a></li>
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
    <a href="#merge-requests">Merge Requests</a>
    <ul>
      <li><a href="#reviewers">Reviewers</a></li>
      <li><a href="#drafts">Drafts</a></li>
      <li><a href="#gitlab-ci">GitLab CI</a></li>
      <li><a href="#merging">Merging</a></li>
    </ul>
  </li>
</ul>
</details>



## Getting Started

Before you begin hacking on `reverse_argparse`, you'll need to do three things:

1. **Request Access:**  On [`reverse_argparse`'s project page](INSERT URL HERE)
   you should see a button to request access to the project.  When you request
   access, a project maintainer will first give you [**Reporter**
   permissions](https://docs.gitlab.com/ee/user/permissions.html).
2. **Fork the Repository:**  Again on [`reverse_argparse`'s project
   page](INSERT URL HERE), in the top-right corner, you'll see a button to
   [fork the repository](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html#creating-a-fork).
   Do so, and then clone your fork and set it up with
   ```bash
   git clone git@server:${USER}/reverse_argparse
   cd reverse_argparse
   git remote add upstream <INSERT UPSTREAM URL>
   git fetch upstream
   ```
3. **Set Up your Environment:**  Install the requirements with
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



## Creating Issues

Create [issues](INSERT URL HERE) in GitLab for any work that needs to be done.
Newly-created issues will automatically go in the **Open** column on the
[Kanban board](INSERT URL HERE).

### Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) is a lightweight markup
language with plain text formatting syntax.  GitLab uses a form of it for
rendering issue and merge request
[descriptions](https://docs.gitlab.com/ee/user/project/issues/issue_data_and_actions.html#description)
and [comments](https://docs.gitlab.com/ee/user/project/issues/issue_data_and_actions.html#comments),
[wiki pages](https://docs.gitlab.com/ee/user/project/wiki/), and
any files in your repositories with a `.md` extension (such as this one).  For
more details on what's possible with GitLab-flavored Markdown, [see GitLab's
documentation on it](https://docs.gitlab.com/ee/user/markdown.html).

### Issue Templates

In the top-left of the page when creating an issue, use the drop-down menu to
select a [description
template](https://docs.gitlab.com/ee/user/project/description_templates.html)
(INSERT AVAILABLE LABELS HERE).  Follow the instructions that appear in the
template.

### Linked Issues

Once an issue has been created, a [**Linked
issues**](https://docs.gitlab.com/ee/user/project/issues/related_issues.html)
box will appear below the issue description.  You can use this feature to
indicate which issues are connected to each other, blocked by one another, etc.

### Labels

The [reverse_argparse > Labels](INSERT URL HERE) page shows you all the labels
we use, along with their descriptions.  "Type" labels will be applied
automatically when an issue is created via the issue template.  "Stage" labels
are used to keep track of how the issue flows through our [Kanban
board](INSERT URL HERE).  Other labels can be added as appropriate.



## Working Issues

### Planning Work

Depending on the needs of the `reverse_argparse` user base, a project
maintainer will schedule issues to be tackled in the near future by dragging
them into the ~"Stage :: Soon" column of the [Kanban board](INSERT URL HERE).
An issue can then be grabbed by a member of the development team when they have
some time available to work on it.

> **Note:**  If you're working on something that hasn't been
> scheduled&mdash;e.g., you're tackling a quick bug fix, or are tinkering with
> a feature you'd like to see added&mdash;don't worry about the
> ~"Stage :: Soon" column; just work on it as per the rest of the guidelines
> below.

### When Work Begins

First move the issue to ~"Stage :: Development" on the [Kanban
board](INSERT URL HERE).  Next make sure your local `master` branch is
up-to-date with
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
work into logical, working commits.  Use either the [Conventional Commit plugin
for Pycharm](https://plugins.jetbrains.com/plugin/13389-conventional-commit) or
the [Conventional Commits extension for VS
Code](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
(or something similar) to ensure your commit messages adhere to the
[Conventional Commits
specification](https://www.conventionalcommits.org/en/v1.0.0/).

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

`reverse_argparse` uses [pytest](https://docs.pytest.org/) for our unit test
suite.  Please add tests to cover any new functions you create.

#### Sphinx

`reverse_argparse` uses [Sphinx](https://www.sphinx-doc.org/en/master/) to
generate [our documentation](INSERT URL HERE).  You'll want to be familiar with
the [Google docstring
format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
and [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
for the sake of updating our documentation while changing the code itself.

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
merge request (see below).

### Closing Old Issues

If at any point you encounter an issue that will not be worked in the
foreseeable future, it is worthwhile to close the issue such that we can
maintain a reasonable backlog of upcoming work.  Do be sure to include in the
comments some explanation as to why the issue won't be addressed.



## Merge Requests

The only way changes get into `master` is through merge requests.  When you've
completed work on an issue, push your branch to your fork with `git push -u
origin <branch-name>`, and then create a merge request.  Remove whatever
"Stage" label GitLab automatically applies, as those only apply to issues.  On
the [Kanban board](INSERT URL HERE), drag your issue into ~"Stage :: Review".

### Reviewers

We recommend having your merge request reviewed by at least two other team
members.  The first should be someone who is knowledgeable about the code that
you're changing&mdash;this is to make sure you don't accidentally do something
foolish.  The second should be someone who knows little about the code you're
touching&mdash;this is to spread the knowledge of how the code works throughout
the team.  Work with your reviewers to get your changes into an acceptable
state.

### Drafts

You may wish to have your changes reviewed by colleagues before they are ready
to be merged into `master`.  To do so, create a merge request as usual, but
insert "Draft:" at the beginning of the title (there will be a link to click to
do this for you).  GitLab will not allow you to merge a draft request.

### GitLab CI

GitLab CI will automatically run on your merge request.  The configuration for
the pipeline can be found in [the `.gitlab-ci.yml` file](INSERT URL HERE) in
the repository root.

### Merging

When the review is finished and changes are ready to be merged into `master`:
1. Rebase your feature branch on top of the latest `master`.
2. Clean up your branch with an interactive rebase, squashing down to the
   smallest number of commits that makes sense.  If there are successive
   distinct changes in a merge request, it's fine for those to be preserved in
   separate commits.
3. Notify your reviewers that the request is ready to merge.
4. Wait for them to merge the request.
5. Ensure the post-merge CI pipeline also succeeds.

> **Note:**  After making it through your first successful merge request into
> `reverse_argparse`, you'll likely be upgraded from **Reporter** to
> [**Developer** permissions](https://docs.gitlab.com/ee/user/permissions.html).
> Once that happens, you can work in the repository itself and no longer need
> your fork (unless you prefer to continue working in it).  Any references to
> `upstream` above can be replaced with `origin`.  Welcome to the team
> :grinning:
