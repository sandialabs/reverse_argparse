![Lines of code](https://sloc.xyz/github/sandialabs/reverse_argparse/?category=code)
[![codecov](https://codecov.io/gh/sandialabs/reverse_argparse/branch/master/graph/badge.svg?token=FmDStZ6FVR)](https://codecov.io/gh/sandialabs/reverse_argparse)
[![CodeFactor](https://www.codefactor.io/repository/github/sandialabs/reverse_argparse/badge/master)](https://www.codefactor.io/repository/github/sandialabs/reverse_argparse/overview/master)
[![CodeQL](https://github.com/sandialabs/reverse_argparse/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/sandialabs/reverse_argparse/actions/workflows/github-code-scanning/codeql)
[![Conda Version](https://img.shields.io/conda/v/conda-forge/reverse-argparse?label=conda-forge)](https://anaconda.org/conda-forge/reverse-argparse)
![Conda Downloads](https://img.shields.io/conda/d/conda-forge/reverse-argparse?label=conda-forge%20downloads)
[![Continuous Integration](https://github.com/sandialabs/reverse_argparse/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/sandialabs/reverse_argparse/actions/workflows/continuous-integration.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![GitHub contributors](https://img.shields.io/github/contributors/sandialabs/reverse_argparse.svg)](https://github.com/sandialabs/reverse_argparse/graphs/contributors)
[![Documentation Status](https://readthedocs.org/projects/reverse-argparse/badge/?version=latest)](https://reverse-argparse.readthedocs.io/en/latest/?badge=latest)
[![License](https://anaconda.org/conda-forge/reverse-argparse/badges/license.svg)](LICENSE.md)
[![Merged PRs](https://img.shields.io/github/issues-pr-closed-raw/sandialabs/reverse_argparse.svg?label=merged+PRs)](https://github.com/sandialabs/reverse_argparse/pulls?q=is:pr+is:merged)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7632/badge)](https://bestpractices.coreinfrastructure.org/projects/7632)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/sandialabs/reverse_argparse/badge)](https://securityscorecards.dev/viewer/?uri=github.com/sandialabs/reverse_argparse)
![Platforms](https://anaconda.org/conda-forge/reverse-argparse/badges/platforms.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci Status](https://results.pre-commit.ci/badge/github/sandialabs/reverse_argparse/master.svg)](https://results.pre-commit.ci/latest/github/sandialabs/reverse_argparse/master)
[![PyPI - Version](https://img.shields.io/pypi/v/reverse-argparse?label=PyPI)](https://pypi.org/project/reverse-argparse/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/reverse-argparse?label=PyPI%20downloads)
![Python Version](https://img.shields.io/badge/Python-3.8|3.9|3.10|3.11|3.12-blue.svg)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# reverse_argparse

Whereas [`argparse`][argparse] is concerned with taking a bunch of command line
arguments and parsing them, this package is intended to do the opposite; that
is, it'll take the parsed arguments and create the effective command line
invocation of the script that generated them.  The motivation is to be able to
tell users exactly what was used for all of the options, taking into
consideration any defaults and other transformations that might've been applied
in the midst of parsing, such that users are able to reproduce a prior run of a
script exactly.

[argparse]: https://docs.python.org/3/library/argparse.html

## Installation

To get up and running with `reverse_argparse`, simply:
```bash
python3 -m pip install reverse-argparse
```

## Usage

Once the package is installed, you can simply
```python
from argparse import ArgumentParser

from reverse_argparse import ReverseArgumentParser

# Parse the command line arguments.
parser = ArgumentParser()
# Build out the parser however you like.
args = parser.parse_args()
# Optionally post-process any `args`, as needed.

# Do whatever you need to in the script.

# Wrap things up.
print("This script executed the following:")
unparser = ReverseArgumentParser(parser, args)
print(unparser.get_pretty_command_line_invocation())
```

For more detailed usage and API information, please see
[our documentation][readthedocs].

[readthedocs]: https://reverse-argparse.readthedocs.io

## Where to Get Help

If you're having trouble with `reverse_argparse`, or just want to ask a
question, head on over to [our issue board][issues].  If a quick search doesn't
yield what you're looking for, feel free to file an issue.

[issues]: https://github.com/sandialabs/reverse_argparse/issues

## Contributing

If you're interested in contributing to the development of `reverse_argparse`,
we'd love to have your help :grinning:  Check out our
[contributing guidelines](CONTRIBUTING.md) for how to get started.
[Past contributors][contributors] include:
* [@jmgate](https://github.com/jmgate)

[contributors]: https://github.com/sandialabs/reverse_argparse/graphs/contributors

## License & Copyright

See [LICENSE.md](LICENSE.md) and [COPYRIGHT.md](COPYRIGHT.md).

## Credits

Special thanks to [@mjsumpter][mjsumpter] for contributing to a prior iteration
of this concept, and to [the GMS project][gms] for investing in the development
of this package.

[mjsumpter]: https://github.com/mjsumpter
[gms]: https://github.com/SNL-GMS/GMS-PI25
