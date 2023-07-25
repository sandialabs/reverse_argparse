[![Code Style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/sandialabs/reverse_argparse/branch/master/graph/badge.svg?token=FmDStZ6FVR)](https://codecov.io/gh/sandialabs/reverse_argparse)
[![Continuous Integration](https://github.com/sandialabs/reverse_argparse/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/sandialabs/reverse_argparse/actions/workflows/continuous-integration.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Documentation Status](https://readthedocs.org/projects/reverse-argparse/badge/?version=latest)](https://reverse-argparse.readthedocs.io/en/latest/?badge=latest)
[![Linting: Pylint](https://img.shields.io/badge/Linting-Pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci Status](https://results.pre-commit.ci/badge/github/sandialabs/reverse_argparse/master.svg)](https://results.pre-commit.ci/latest/github/sandialabs/reverse_argparse/master)
[![PyPI Version](https://badge.fury.io/py/reverse_argparse.svg)](https://badge.fury.io/py/reverse-argparse)
![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
[![Security: Bandit](https://img.shields.io/badge/Security-Bandit-yellow.svg)](https://github.com/PyCQA/bandit)

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

## License

See [LICENSE.md](LICENSE.md).

## Credits

Special thanks to [the GMS project][gms] for investing in the initial
development of this package.

[gms]: https://github.com/SNL-GMS/GMS-PI21-OPEN/
