"""
The ``reverse_argparse`` package.

Provide the :class:`ReverseArgumentParser` class and
:func:`quote_arg_if_necessary` helper function.

Copyright The reverse-argparse Authors.
SPDX-License-Identifier: BSD-3-Clause
"""

from .reverse_argparse import ReverseArgumentParser, quote_arg_if_necessary

__all__ = ["ReverseArgumentParser", "quote_arg_if_necessary"]
__version__ = "1.0.6"
