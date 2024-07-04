#!/usr/bin/env python3
"""How ``reverse_argparse`` handles subparsers."""

# © 2023 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import os
from argparse import ArgumentParser

import dateparser

from reverse_argparse import ReverseArgumentParser

parser = ArgumentParser()
subparsers = parser.add_subparsers(title="Subcommands")
foo_parser = subparsers.add_parser("foo")
foo_parser.add_argument("--one")
foo_parser.add_argument("--two", default="spam")
foo_parser.add_argument("--three", type=int, default=42)
bar_parser = subparsers.add_parser("bar")
bar_parser.add_argument(
    "--four",
    type=os.path.abspath,  # type: ignore[arg-type]
)
bar_parser.add_argument("--five")

# Parse the command line arguments.
args = parser.parse_args()
if getattr(args, "five", None) is not None:
    args.five = dateparser.parse(args.five)

# Insert the body of your script here.

# Unparse the arguments to tell the user what they ran.
print("The effective command line invocation was:")
unparser = ReverseArgumentParser(parser, args)
print(unparser.get_pretty_command_line_invocation())
