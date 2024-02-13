#!/usr/bin/env python3
"""
Run all the examples and ensure their output is correct.

Copyright The reverse-argparse Authors.
SPDX-License-Identifier: BSD-3-Clause
"""
import re
import shlex
import subprocess  # nosec B404
from datetime import datetime, timedelta
from pathlib import Path


def test_basic() -> None:
    example = Path(__file__).parent / "basic.py"
    result = subprocess.run(
        [example, "--foo", "bar"],
        capture_output=True,
        check=True,
        text=True,
    )  # nosec B603
    assert (
        result.stdout
        == """
The effective command line invocation was:
basic.py --foo bar
""".lstrip()
    )


def test_default_values() -> None:
    example = Path(__file__).parent / "default_values.py"
    result = subprocess.run(
        [example, "--foo", "bar"],
        capture_output=True,
        check=True,
        text=True,
    )  # nosec B603
    assert (
        result.stdout
        == """
The effective command line invocation was:
default_values.py --foo bar --bar spam --baz 42
""".lstrip()
    )


def test_relative_references() -> None:
    example = Path(__file__).parent / "relative_references.py"
    result = subprocess.run(
        [example, "--src", "bar.txt"],
        capture_output=True,
        check=True,
        text=True,
    )  # nosec B603
    assert (
        """
The effective command line invocation was:
relative_references.py --bar spam --baz 42 --src
""".strip()
        in result.stdout
    )
    assert re.search(r"--src /\S+/bar\.txt", result.stdout)


def test_post_processing() -> None:
    example = Path(__file__).parent / "post_processing.py"
    result = subprocess.run(
        [example, "--before", "'30 minutes ago'"],
        capture_output=True,
        check=True,
        text=True,
    )  # nosec B603
    assert (
        """
The effective command line invocation was:
post_processing.py --bar spam --baz 42 --before
""".strip()
        in result.stdout
    )
    thirty_miutes_ago = datetime.now() - timedelta(minutes=30)
    time_from_example = datetime.strptime(
        shlex.split(result.stdout)[-1], "%Y-%m-%d %H:%M:%S.%f"
    )
    assert thirty_miutes_ago - time_from_example < timedelta(seconds=1)


def test_pretty_printing() -> None:
    example = Path(__file__).parent / "pretty_printing.py"
    result = subprocess.run(
        [example, "--foo", "eggs", "--src", "file.txt", "--before", "'today'"],
        capture_output=True,
        check=True,
        text=True,
    )  # nosec B603
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
    today = datetime.now()
    time_from_example = datetime.strptime(
        shlex.split(result.stdout.splitlines()[-1])[-1],
        "%Y-%m-%d %H:%M:%S.%f",
    )
    assert today - time_from_example < timedelta(seconds=1)


def test_subparsers() -> None:
    example = Path(__file__).parent / "subparsers.py"
    result = subprocess.run(
        [example, "foo", "--one", "eggs"],
        capture_output=True,
        check=True,
        text=True,
    )  # nosec B603
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
