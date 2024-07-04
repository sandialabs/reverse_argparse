"""
The ``reverse_argparse`` package.

Provide the :class:`ReverseArgumentParser` class and
:func:`quote_arg_if_necessary` helper function.
"""

# © 2023 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

from .reverse_argparse import ReverseArgumentParser, quote_arg_if_necessary

__all__ = ["ReverseArgumentParser", "quote_arg_if_necessary"]
__version__ = "1.0.8"
