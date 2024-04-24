reverse_argparse
================

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   motivation
   examples
   reference

|Code lines|
|codecov|
|CodeFactor|
|CodeQL|
|conda-forge Version|
|conda-forge Downloads|
|Continuous Integration|
|Contributor Covenant|
|GitHub Contributors|
|Documentation Status|
|License|
|Merged PRs|
|OpenSSF Best Practices|
|OpenSSF Scorecard|
|Platforms|
|pre-commit|
|pre-commit.ci Status|
|PyPI Version|
|PyPI Downloads|
|Python Version|
|Ruff|

.. |Code lines| image:: https://sloc.xyz/github/sandialabs/reverse_argparse/?category=code
.. |codecov| image:: https://codecov.io/gh/sandialabs/reverse_argparse/branch/master/graph/badge.svg?token=FmDStZ6FVR
   :target: https://codecov.io/gh/sandialabs/reverse_argparse
.. |CodeFactor| image:: https://www.codefactor.io/repository/github/sandialabs/reverse_argparse/badge/master
   :target: https://www.codefactor.io/repository/github/sandialabs/reverse_argparse/overview/master
.. |CodeQL| image:: https://github.com/sandialabs/reverse_argparse/actions/workflows/github-code-scanning/codeql/badge.svg
   :target: https://github.com/sandialabs/reverse_argparse/actions/workflows/github-code-scanning/codeql
.. |conda-forge Version| image:: https://img.shields.io/conda/v/conda-forge/reverse-argparse?label=conda-forge
   :target: https://anaconda.org/conda-forge/reverse-argparse
.. |conda-forge Downloads| image:: https://img.shields.io/conda/d/conda-forge/reverse-argparse?label=conda-forge%20downloads
.. |Continuous Integration| image:: https://github.com/sandialabs/reverse_argparse/actions/workflows/continuous-integration.yml/badge.svg
   :target: https://github.com/sandialabs/reverse_argparse/actions/workflows/continuous-integration.yml
.. |Contributor Covenant| image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: https://github.com/sandialabs/reverse_argparse/blob/master/CODE_OF_CONDUCT.md
.. |GitHub Contributors| image:: https://img.shields.io/github/contributors/sandialabs/reverse_argparse.svg
   :target: https://github.com/sandialabs/reverse_argparse/graphs/contributors
.. |Documentation Status| image:: https://readthedocs.org/projects/reverse-argparse/badge/?version=latest
   :target: https://reverse-argparse.readthedocs.io/en/latest/?badge=latest
.. |License| image:: https://anaconda.org/conda-forge/reverse-argparse/badges/license.svg
   :target: https://github.com/sandialabs/reverse_argparse/blob/master/LICENSE.md
.. |Merged PRs| image:: https://img.shields.io/github/issues-pr-closed-raw/sandialabs/reverse_argparse.svg?label=merged+PRs
   :target: https://github.com/sandialabs/reverse_argparse/pulls?q=is:pr+is:merged
.. |OpenSSF Best Practices| image:: https://bestpractices.coreinfrastructure.org/projects/7632/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/7632
.. |OpenSSF Scorecard| image:: https://api.securityscorecards.dev/projects/github.com/sandialabs/reverse_argparse/badge
   :target: https://securityscorecards.dev/viewer/?uri=github.com/sandialabs/reverse_argparse
.. |Platforms| image:: https://anaconda.org/conda-forge/reverse-argparse/badges/platforms.svg
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit
.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/sandialabs/reverse_argparse/master.svg
   :target: https://results.pre-commit.ci/latest/github/sandialabs/reverse_argparse/master
.. |PyPI Version| image:: https://img.shields.io/pypi/v/reverse-argparse?label=PyPI
   :target: https://pypi.org/project/reverse-argparse/
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/reverse-argparse?label=PyPI%20downloads
.. |Python Version| image:: https://img.shields.io/badge/Python-3.8|3.9|3.10|3.11|3.12-blue.svg
.. |Ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff

The ``reverse_argparse`` module provides a means of undoing the argument
parsing provided by :mod:`argparse`.  That is, it can take a
:class:`argparse.Namespace` of parsed command line arguments, along with the
:class:`argparse.ArgumentParser` that generated it, and then unparse everything
into the exact list of command line arguments that was used when executing the
script.

"But wait, if I just ran a script on the command line, I can see what I just
typed in.  Why would the script need to figure that out again so it could tell
me something I can see right in front of me?"

Because ``reverse_argparse`` will take into consideration any default values,
along with any transformations that have been made after argument parsing
(e.g., path resolution, etc.).  For more details on why this matters, check out
the :doc:`motivation` page.

Installation
------------

To get up and running with ``reverse_argparse``, simply

.. code-block:: bash

   python3 -m pip install reverse-argparse

Usage
-----

Once the package is installed, you can simply

.. code-block:: python
   :emphasize-lines: 3,13-16

   from argparse import ArgumentParser

   from reverse_argparse import ReverseArgumentParser

   # Parse the command line arguments.
   parser = ArgumentParser()
   # Build out the parser however you like.
   args = parser.parse_args()
   # Optionally post-process any arguments, as needed.

   # Do whatever you need to in the script.

   # Wrap things up.
   print("This script executed the following:")
   unparser = ReverseArgumentParser(parser, args)
   print(unparser.get_pretty_command_line_invocation())

For more detailed usage information, see the :doc:`examples` page.  For
implementation details, see the :doc:`reference documentation <reference>`.

Contributing
------------

The source repository for this module is `on GitHub`_.  See the project's
README and contributing guidelines for details on how to interact with the
project.

.. _on GitHub:  https://github.com/sandialabs/reverse_argparse
