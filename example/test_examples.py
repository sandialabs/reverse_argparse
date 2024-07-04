#!/usr/bin/env python3
"""Run all the examples and ensure their output is correct."""

# © 2023 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import re
import shlex
import subprocess  # nosec B404
from datetime import datetime, timedelta, timezone
from pathlib import Path


def test_basic() -> None:
    """Ensure ``basic.py`` produces the expected results."""
    example = Path(__file__).parent / "basic.py"
    result = subprocess.run(
        [example, "--foo", "bar"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert (
        result.stdout
        == """
The effective command line invocation was:
basic.py --foo bar
""".lstrip()
    )


def test_default_values() -> None:
    """Ensure ``default_values.py`` produces the expected results."""
    example = Path(__file__).parent / "default_values.py"
    result = subprocess.run(
        [example, "--foo", "bar"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert (
        result.stdout
        == """
The effective command line invocation was:
default_values.py --foo bar --bar spam --baz 42
""".lstrip()
    )


def test_relative_references() -> None:
    """Ensure ``relative_references.py`` produces the expected results."""
    example = Path(__file__).parent / "relative_references.py"
    result = subprocess.run(
        [example, "--src", "bar.txt"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert (
        """
The effective command line invocation was:
relative_references.py --bar spam --baz 42 --src
""".strip()
        in result.stdout
    )
    assert re.search(r"--src /\S+/bar\.txt", result.stdout)


def test_post_processing() -> None:
    """Ensure ``post_processing.py`` produces the expected results."""
    example = Path(__file__).parent / "post_processing.py"
    result = subprocess.run(
        [example, "--before", "'30 minutes ago'"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert (
        """
The effective command line invocation was:
post_processing.py --bar spam --baz 42 --before
""".strip()
        in result.stdout
    )
    thirty_miutes_ago = datetime.now(tz=timezone.utc) - timedelta(minutes=30)
    time_from_example = datetime.strptime(
        shlex.split(result.stdout)[-1], "%Y-%m-%d %H:%M:%S.%f"
    ).astimezone(timezone.utc)
    assert thirty_miutes_ago - time_from_example < timedelta(seconds=1)


def test_pretty_printing() -> None:
    """Ensure ``pretty_printing.py`` produces the expected results."""
    example = Path(__file__).parent / "pretty_printing.py"
    result = subprocess.run(
        [
            example,
            "--foo",
            "eggs",
            "--src",
            "file.txt",
            "--before",
            "'today'",
        ],
        capture_output=True,
        check=True,
        text=True,
    )
    assert (
        """
The effective command line invocation was:
pretty_printing.py \\
    --foo eggs \\
    --bar spam \\
    --baz 42 \\
""".strip()
        in result.stdout
    )
    assert re.search(r"--src /\S+/file\.txt", result.stdout)
    today = datetime.now(tz=timezone.utc)
    time_from_example = datetime.strptime(
        shlex.split(result.stdout.splitlines()[-1])[-1],
        "%Y-%m-%d %H:%M:%S.%f",
    ).astimezone(timezone.utc)
    assert today - time_from_example < timedelta(seconds=1)


def test_subparsers() -> None:
    """Ensure ``subparsers.py`` produces the expected results."""
    example = Path(__file__).parent / "subparsers.py"
    result = subprocess.run(
        [example, "foo", "--one", "eggs"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert (
        result.stdout
        == """
The effective command line invocation was:
subparsers.py \\
    foo \\
        --one eggs \\
        --two spam \\
        --three 42
""".lstrip()
    )
