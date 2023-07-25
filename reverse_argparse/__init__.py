"""
The ``reverse_argparse`` package.

Provide the :class:`ReverseArgumentParser` class and
:func:`quote_arg_if_necessary` helper function.
"""
from .reverse_argparse import ReverseArgumentParser, quote_arg_if_necessary

__all__ = ["ReverseArgumentParser", "quote_arg_if_necessary"]
__version__ = "1.0.3"
