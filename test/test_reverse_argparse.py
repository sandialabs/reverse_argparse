"""The unit test suite for the ``reverse_argparse`` package."""

# © 2023 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import shlex
import sys
from argparse import SUPPRESS, ArgumentParser, Namespace

import pytest

from reverse_argparse import ReverseArgumentParser


BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION = 9


if sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION:
    from argparse import BooleanOptionalAction


@pytest.fixture()
def parser() -> ArgumentParser:
    """
    Pre-populate an ``ArgumentParser`` with a variety of options.

    Returns:
        The ``ArgumentParser`` to be used in a number of tests.
    """
    p = ArgumentParser()
    p.add_argument("pos1", nargs="*")
    p.add_argument("pos2")
    p.add_argument("--opt1")
    p.add_argument("--opt2", nargs="*")
    p.add_argument("--store-true", action="store_true")
    p.add_argument("--store-false", action="store_false")
    p.add_argument("--needs-quotes")
    p.add_argument("--default", default=42)
    p.add_argument("--app1", action="append")
    p.add_argument("--app2", action="append")
    p.add_argument("--app-nargs", action="append", nargs="*")
    p.add_argument("--const", action="store_const", const=42)
    p.add_argument(
        "--app-const1", dest="app_const", action="append_const", const=42
    )
    p.add_argument(
        "--app-const2", dest="app_const", action="append_const", const=53
    )
    p.add_argument("--verbose", "-v", action="count", default=2)
    p.add_argument("--ext", action="extend", nargs="*")
    if sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION:
        p.add_argument(
            "--bool-opt", action=BooleanOptionalAction, default=False
        )
    return p


COMPLETE_ARGS = [
    "pos1-val1 pos1-val2 "
    "pos2-val "
    "--ext ext-val1 "
    "--app-nargs app-nargs1-val1 app-nargs1-val2 "
    "--app-const1 "
    "--ext ext-val2 ext-val3 "
    "--opt1 opt1-val "
    "-vv "
    "--app1 app1-val1 "
    "--app1 app1-val2 "
    "--opt2 opt2-val1 opt2-val2 "
    "--app2 app2-val1 "
    "--const "
    "--store-true "
    "--app2 app2-val2 "
    "--store-false "
    "--app-const2 "
    "--app-nargs app-nargs2-val "
    "--needs-quotes 'hello world'",
    "--ext ext-val1 "
    "--app-nargs app-nargs1-val1 app-nargs1-val2 "
    "--app-const1 "
    "--ext ext-val2 ext-val3 "
    "--opt1 opt1-val "
    "-vv "
    "--app1 app1-val1 "
    "--app1 app1-val2 "
    "--opt2 opt2-val1 opt2-val2 "
    "--app2 app2-val1 "
    "--const "
    "--store-true "
    "--app2 app2-val2 "
    "--store-false "
    "--app-const2 "
    "--app-nargs app-nargs2-val "
    "--needs-quotes 'hello world' "
    "-- "
    "pos1-val1 pos1-val2 "
    "pos2-val",
]


def strip_first_entry(input_string: str) -> str:
    """
    Remove the first entry of a space-delimited string.

    Args:
        input_string:  A space-delimited string.

    Returns:
        The input string with the first element (and first space)
        removed.
    """
    return " ".join(input_string.split()[1:])


def test_strip_first_entry() -> None:
    """Ensure :func:`strip_first_entry` works as expected."""
    assert strip_first_entry("foo bar baz") == "bar baz"


def strip_first_line(input_string: str) -> str:
    """
    Remove the first line of a multi-line string.

    Args:
        input_string:  A multi-line string.

    Returns:
        The input string with the first line removed.
    """
    return "\n".join(input_string.splitlines()[1:])


def test_strip_first_line() -> None:
    """Ensure :func:`strip_first_line` works as expected."""
    assert strip_first_line("foo\nbar\nbaz") == "bar\nbaz"


@pytest.mark.parametrize("args", COMPLETE_ARGS)
def test_get_effective_command_line_invocation(parser, args) -> None:
    """Ensure :func:`get_effective_command_line_invoation` works."""
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = (
        (
            "--opt1 opt1-val --opt2 opt2-val1 opt2-val2 --store-true "
            "--store-false --needs-quotes 'hello world' --default 42 --app1 "
            "app1-val1 --app1 app1-val2 --app2 app2-val1 --app2 app2-val2 "
            "--app-nargs app-nargs1-val1 app-nargs1-val2 --app-nargs "
            "app-nargs2-val --const --app-const1 --app-const2 -vv --ext "
            "ext-val1 ext-val2 ext-val3 "
        )
        + (
            "--no-bool-opt "
            if sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION
            else ""
        )
        + "pos1-val1 pos1-val2 pos2-val"
    )
    result = strip_first_entry(
        unparser.get_effective_command_line_invocation()
    )
    assert result == expected


@pytest.mark.parametrize("args", COMPLETE_ARGS)
def test_get_pretty_command_line_invocation(parser, args) -> None:
    """Ensure :func:`get_pretty_command_line_invoation` works as expected."""
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = """    --opt1 opt1-val \\
    --opt2 opt2-val1 opt2-val2 \\
    --store-true \\
    --store-false \\
    --needs-quotes 'hello world' \\
    --default 42 \\
    --app1 app1-val1 \\
    --app1 app1-val2 \\
    --app2 app2-val1 \\
    --app2 app2-val2 \\
    --app-nargs app-nargs1-val1 app-nargs1-val2 \\
    --app-nargs app-nargs2-val \\
    --const \\
    --app-const1 \\
    --app-const2 \\
    -vv \\
    --ext ext-val1 ext-val2 ext-val3 \\"""
    if sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION:
        expected += "\n    --no-bool-opt \\"
    expected += """\n    pos1-val1 pos1-val2 \\
    pos2-val"""
    result = strip_first_line(unparser.get_pretty_command_line_invocation())
    assert result == expected


def test_get_command_line_invocation_strip_spaces() -> None:
    """Ensure extraneous spaces are stripped."""
    parser = ArgumentParser()
    namespace = Namespace()
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._args = ["program_name", "    --foo", "    ", "    --bar"]
    unparser._unparsed = [True]
    expected = "program_name --foo --bar"
    assert unparser.get_effective_command_line_invocation() == expected
    expected = """    --foo \\
    --bar"""
    result = strip_first_line(unparser.get_pretty_command_line_invocation())
    assert result == expected


@pytest.mark.parametrize(
    ("add_args", "add_kwargs", "args", "expected"),
    [
        (["--foo"], {"action": "store"}, "--foo bar", ["    --foo bar"]),
        (
            ["--foo"],
            {"action": "store_const", "const": 42},
            "--foo",
            ["    --foo"],
        ),
        (["--foo"], {"action": "store_true"}, "--foo", ["    --foo"]),
        (["--foo"], {"action": "store_false"}, "--foo", ["    --foo"]),
        (
            ["--foo"],
            {"action": "append"},
            "--foo bar --foo baz",
            ["    --foo bar", "    --foo baz"],
        ),
        (
            ["--foo"],
            {"dest": "append_const", "action": "append_const", "const": 42},
            "--foo",
            ["    --foo"],
        ),
        (
            ["--foo", "-f"],
            {"action": "count", "default": 0},
            "--foo --foo",
            ["    -ff"],
        ),
        (["--foo"], {"action": "help"}, "--foo", []),
        (["--foo"], {"action": "version", "version": "1.2.3"}, "--foo", []),
        (
            ["--foo"],
            {"action": "extend", "nargs": "*"},
            "--foo bar --foo baz bif",
            ["    --foo bar baz bif"],
        ),
    ],
)
def test__unparse_args(add_args, add_kwargs, args, expected) -> None:
    """Ensure :func:`_unparse_args` works as expected."""
    parser = ArgumentParser()
    parser.add_argument(*add_args, **add_kwargs)
    try:
        namespace = parser.parse_args(shlex.split(args))
    except SystemExit:
        namespace = Namespace()
    unparser = ReverseArgumentParser(parser, namespace)
    if expected == "NotImplemented":
        with pytest.raises(NotImplementedError):
            unparser._unparse_args()
    else:
        unparser._unparse_args()
        assert unparser._args[1:] == expected


def test__unparse_args_boolean_optional_action() -> None:
    """
    Ensure :func:`_unparse_args` works as expected.

    With a ``BooleanOptionalAction``, which became available in Python
    3.9.
    """
    if sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION:
        parser = ArgumentParser()
        parser.add_argument("--foo", action=BooleanOptionalAction)
        try:
            namespace = parser.parse_args(shlex.split("--foo"))
        except SystemExit:
            namespace = Namespace()
        unparser = ReverseArgumentParser(parser, namespace)
        unparser._unparse_args()
        assert unparser._args[1:] == ["    --foo"]


def test__unparse_args_already_unparsed() -> None:
    """Ensure unparsing is a no-op if the args have already been unparsed."""
    parser = ArgumentParser()
    namespace = Namespace()
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._args = ["program_name", "    --ensure args", "   unchanged"]
    args_before = unparser._args.copy()
    unparser._unparsed = [True]
    unparser._unparse_args()
    assert unparser._args == args_before


def test__arg_is_default_and_help_is_suppressed() -> None:
    """Ensure defaults for suppressed args are suppressed."""
    parser = ArgumentParser()
    parser.add_argument("--suppressed", default=10, help=SUPPRESS)
    namespace = parser.parse_args(shlex.split(""))
    unparser = ReverseArgumentParser(parser, namespace)
    result = strip_first_entry(
        unparser.get_effective_command_line_invocation()
    )
    assert result == ""


@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        (["-v", "--verbose"], ["--verbose"]),
        (["--foo", "-f", "--foo-bar"], ["--foo", "--foo-bar"]),
        (["-x"], []),
    ],
)
def test__get_long_option_strings(strings, expected) -> None:
    """Ensure the long-form option is selected from a list."""
    unparser = ReverseArgumentParser(ArgumentParser(), Namespace())
    assert unparser._get_long_option_strings(strings) == expected


@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        (["-v", "--verbose"], ["-v"]),
        (["--foo", "-f", "--foo-bar"], ["-f"]),
        (["--foo"], []),
    ],
)
def test__get_short_option_strings(strings, expected) -> None:
    """Ensure the short-form option is selected from a list."""
    unparser = ReverseArgumentParser(ArgumentParser(), Namespace())
    assert unparser._get_short_option_strings(strings) == expected


@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        (["-v", "--verbose"], "--verbose"),
        (["--foo", "-f", "--foo-bar"], "--foo"),
        (["-x"], "-x"),
    ],
)
def test__get_option_string(strings, expected) -> None:
    """Ensure long-form options are preferred over short-form ones."""
    parser = ArgumentParser()
    action = parser.add_argument(*strings)
    unparser = ReverseArgumentParser(parser, Namespace())
    assert unparser._get_option_string(action) == expected


@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        (["-v", "--verbose"], "-v"),
        (["-f", "--foo", "-b"], "-f"),
        (["--foo"], "--foo"),
    ],
)
def test__get_option_string_prefer_short(strings, expected) -> None:
    """Ensure short-form options are preferred over long-form ones."""
    parser = ArgumentParser()
    action = parser.add_argument(*strings)
    unparser = ReverseArgumentParser(parser, Namespace())
    assert unparser._get_option_string(action, prefer_short=True) == expected


@pytest.mark.parametrize(
    ("add_args", "add_kwargs", "args", "expected"),
    [
        (["positional"], {}, "val", "    val"),
        (["-f", "--foo"], {}, "-f bar", "    --foo bar"),
        (["-f"], {}, "-f bar", "    -f bar"),
        (["--foo", "--foo-bar"], {}, "--foo-bar baz", "    --foo baz"),
        (["positional"], {"nargs": "*"}, "val1 val2", "    val1 val2"),
        (["-f", "--foo"], {"nargs": "*"}, "-f bar baz", "    --foo bar baz"),
        (["-f"], {"nargs": "*"}, "-f bar baz", "    -f bar baz"),
        (
            ["--foo", "--foo-bar"],
            {"nargs": "*"},
            "--foo-bar baz bif",
            "    --foo baz bif",
        ),
    ],
)
def test__unparse_store_action(add_args, add_kwargs, args, expected) -> None:
    """Ensure ``store`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_store_action(action)
    assert unparser._args[1:] == [expected]


@pytest.mark.parametrize(
    ("add_args", "add_kwargs", "args", "expected"),
    [
        (["--foo"], {"action": "store_const", "const": 42}, "", None),
        (
            ["--foo"],
            {"action": "store_const", "const": 42},
            "--foo",
            "    --foo",
        ),
        (
            ["--foo"],
            {"action": "store_const", "const": 42, "default": 53},
            "",
            None,
        ),
        (
            ["--foo"],
            {"action": "store_const", "const": 42, "default": 53},
            "--foo",
            "    --foo",
        ),
    ],
)
def test__unparse_store_const_action(
    add_args, add_kwargs, args, expected
) -> None:
    """Ensure ``store_const`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_store_const_action(action)
    assert unparser._args[1:] == ([expected] if expected is not None else [])


@pytest.mark.parametrize(
    ("args", "expected"), [(shlex.split("--foo"), "    --foo"), ([], None)]
)
def test__unparse_store_true_action(args, expected) -> None:
    """Ensure ``store_true`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument("--foo", action="store_true")
    namespace = parser.parse_args(args)
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_store_true_action(action)
    assert unparser._args[1:] == ([expected] if expected is not None else [])


@pytest.mark.parametrize(
    ("args", "expected"), [(shlex.split("--foo"), "    --foo"), ([], None)]
)
def test__unparse_store_false_action(args, expected) -> None:
    """Ensure ``store_false`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument("--foo", action="store_false")
    namespace = parser.parse_args(args)
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_store_false_action(action)
    assert unparser._args[1:] == ([expected] if expected is not None else [])


@pytest.mark.parametrize(
    ("add_args", "add_kwargs", "args", "expected"),
    [
        (
            ["--foo"],
            {"action": "append"},
            "--foo bar --foo baz",
            ["    --foo bar", "    --foo baz"],
        ),
        (
            ["--foo"],
            {"action": "append", "nargs": "*"},
            "--foo bar baz --foo bif",
            ["    --foo bar baz", "    --foo bif"],
        ),
    ],
)
def test__unparse_append_action(add_args, add_kwargs, args, expected) -> None:
    """Ensure ``append`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_append_action(action)
    assert unparser._args[1:] == expected


@pytest.mark.parametrize(
    ("args", "expected"), [("--foo", "    --foo"), ("", None)]
)
def test__unparse_append_const_action(args, expected) -> None:
    """Ensure ``append_const`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument(
        "--foo", dest="append_const", action="append_const", const=42
    )
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_append_const_action(action)
    assert unparser._args[1:] == ([expected] if expected is not None else [])


@pytest.mark.parametrize(
    ("add_args", "add_kwargs", "args", "expected"),
    [
        (
            ["--foo"],
            {"action": "count"},
            "--foo --foo --foo",
            "    --foo --foo --foo",
        ),
        (
            ["--verbose", "-v"],
            {"action": "count"},
            "--verbose -v --verbose",
            "    -vvv",
        ),
        (
            ["--verbose", "-v"],
            {"action": "count", "default": 2},
            "-vv",
            "    -vv",
        ),
    ],
)
def test__unparse_count_action(add_args, add_kwargs, args, expected) -> None:
    """Ensure ``count`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_count_action(action)
    assert unparser._args[1:] == [expected]


@pytest.mark.parametrize(
    ("args", "expected", "pretty"),
    [
        ("a 12", "a 12", "    a \\\n        12"),
        (
            "--foo b --baz Z",
            "--foo b --baz Z",
            "    --foo \\\n    b \\\n        --baz Z",
        ),
    ],
)
def test__unparse_sub_parsers_action(args, expected, pretty) -> None:
    """Ensure subparsers are handled appropriately."""
    parser = ArgumentParser()
    parser.add_argument("--foo", action="store_true", help="foo help")
    subparsers = parser.add_subparsers(help="sub-command help")
    parser_a = subparsers.add_parser("a", help="a help")
    parser_a.add_argument("bar", type=int, help="bar help")
    parser_b = subparsers.add_parser("b", help="b help")
    parser_b.add_argument("--baz", choices="XYZ", help="baz help")
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_args()
    result = strip_first_entry(
        unparser.get_effective_command_line_invocation()
    )
    assert result == expected
    result = strip_first_line(unparser.get_pretty_command_line_invocation())
    assert result == pretty


def test__unparse_sub_parsers_action_nested() -> None:
    """Ensure nested subparsers are handled appropriately."""
    parser = ArgumentParser()
    parser.add_argument("--optional-1", action="store_true")
    parser.add_argument("--optional-2")
    parser.add_argument("positional-1")
    parser.add_argument("positional-2", nargs="*")
    subparsers = parser.add_subparsers()
    subcommand = subparsers.add_parser("subcommand")
    subcommand.add_argument("--sub-optional")
    subcommand.add_argument("sub-positional")
    subsubparsers = subcommand.add_subparsers()
    subsubcommand = subsubparsers.add_parser("subsubcommand")
    subsubcommand.add_argument("--sub-sub-optional", action="store_false")
    subsubcommand.add_argument("sub-sub-positional")
    args = (
        "--optional-1 --optional-2 optional-2-arg positional-1-arg "
        "positional-2-arg-1 positional-2-arg-2 subcommand --sub-optional "
        "sub-optional-arg sub-positional-arg subsubcommand --sub-sub-optional "
        "sub-sub-positional-arg"
    )
    pretty = """    --optional-1 \\
    --optional-2 optional-2-arg \\
    positional-1-arg \\
    positional-2-arg-1 positional-2-arg-2 \\
    subcommand \\
        --sub-optional sub-optional-arg \\
        sub-positional-arg \\
        subsubcommand \\
            --sub-sub-optional \\
            sub-sub-positional-arg"""
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    unparser._unparse_args()
    result = strip_first_entry(
        unparser.get_effective_command_line_invocation()
    )
    assert result == args
    result = strip_first_line(unparser.get_pretty_command_line_invocation())
    assert result == pretty


def test__unparse_extend_action() -> None:
    """Ensure ``extend`` actions are handled appropriately."""
    parser = ArgumentParser()
    action = parser.add_argument("--foo", action="extend", nargs="*")
    namespace = parser.parse_args(shlex.split("--foo bar --foo baz bif"))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = "    --foo bar baz bif"
    unparser._unparse_extend_action(action)
    assert unparser._args[1:] == [expected]


@pytest.mark.parametrize(
    ("default", "args", "expected"),
    [
        (None, "", None),
        (None, "--bool-opt", "    --bool-opt"),
        (None, "--no-bool-opt", "    --no-bool-opt"),
        (True, "", "    --bool-opt"),
        (True, "--bool-opt", "    --bool-opt"),
        (True, "--no-bool-opt", "    --no-bool-opt"),
        (False, "", "    --no-bool-opt"),
        (False, "--bool-opt", "    --bool-opt"),
        (False, "--no-bool-opt", "    --no-bool-opt"),
    ],
)
def test__unparse_boolean_optional_action(default, args, expected) -> None:
    """Ensure ``BooleanOptionalAction`` actions are handled appropriately."""
    if sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION:
        parser = ArgumentParser()
        action = parser.add_argument(
            "--bool-opt", action=BooleanOptionalAction, default=default
        )
        namespace = parser.parse_args(shlex.split(args))
        unparser = ReverseArgumentParser(parser, namespace)
        unparser._unparse_boolean_optional_action(action)
        assert unparser._args[1:] == (
            [expected] if expected is not None else []
        )
