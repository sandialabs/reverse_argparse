[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

# reverse_argparse

Whereas [`argparse`](https://docs.python.org/3/library/argparse.html) is
concerned with taking a bunch of command line arguments and parsing them, this
package is intended to do the opposite; that is, it'll take the parsed
arguments and create the effective command line invocation of the script that
generated them.  The motivation is to be able to tell users exactly what was
used for all of the options, taking into consideration any defaults and other
transformations that might've been applied in the midst of parsing, such that
users are able to reproduce a prior run of a script exactly.

## Installation

To get up and running with `reverse_argparse`, simply:
```bash
pip install reverse_argparse
```

> **Note:**  This won't actually work until the package has been published to
> PyPI.

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

For more detailed usage and API information, please see [our
documentation](INSERT URL HERE).

## Where to Get Help

If you're having trouble with `reverse_argparse`, or just want to ask a
question, head on over to [our issue board](INSERT URL HERE).  If a quick
search doesn't yield what you're looking for, feel free to file an issue.

## Contributing

If you're interested in contributing to the development of `reverse_argparse`,
we'd love to have your help :grinning:  Check out our [contributing
guidelines](INSERT URL HERE) for how to get started.  [Past
contributors](INSERT URL HERE) include:
* @jmgate

## License

License information will be added after `reverse_argparse` makes it through our
open-sourcing process.

## Credits

Special thanks to [the GMS project](INSERT URL HERE) for investing in the
initial development of this package.
