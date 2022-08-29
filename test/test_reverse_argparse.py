#!/usr/bin/env python3

import shlex
from argparse import ArgumentParser, BooleanOptionalAction, Namespace
from unittest.mock import patch

import pytest
from python.reverse_argparse.reverse_argparse.reverse_argparse import \
    ReverseArgumentParser


@patch(
    "python.reverse_argparse.reverse_argparse.reverse_argparse."
    "ReverseArgumentParser._unparse_action"
)
def test__get_args(mock__unparse_action) -> None:
    results = [
        ["pos1", "pos2"],
        ["--opt", "val"],
        [],
        ["--store-true"],
        [],
    ]  # yapf: disable
    mock__unparse_action.side_effect = results
    unparser = ReverseArgumentParser(ArgumentParser(), Namespace())
    assert unparser._get_args(results) == [
        ["pos1", "pos2"],
        ["--opt", "val"],
        ["--store-true"],
    ]  # yapf: disable


@pytest.mark.parametrize(
    "args, expected",
    [(
        "--opt1 opt1-val --opt2 opt2-val1 opt2-val2",
        [["--opt1", "opt1-val"], ["--opt2", "opt2-val1", "opt2-val2"]]
    ), (
        "--store-true --store-false",
        [["--store-true"], ["--store-false"]]
    ), (
        "--needs-quotes 'hello world'",
        [["--needs-quotes", "'hello world'"]]
    ), (
        "--append one two --append three",
        [["--append", "one", "two"], ["--append", "three"]]
    )]
)  # yapf: disable
def test_get_optional_args(args, expected) -> None:
    parser = ArgumentParser()
    parser.add_argument("--opt1")
    parser.add_argument("--opt2", nargs="*")
    parser.add_argument("--store-true", action="store_true")
    parser.add_argument("--store-false", action="store_false")
    parser.add_argument("--needs-quotes")
    parser.add_argument("--append", action="append", nargs="*")
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser.get_optional_args() == expected


def test_get_positional_args() -> None:
    parser = ArgumentParser()
    parser.add_argument("pos1")
    parser.add_argument("pos2", nargs="*")
    args = "pos1-val pos2-val1 pos2-val2 'needs quotes'"
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = [["pos1-val"], ["pos2-val1", "pos2-val2", "'needs quotes'"]]
    assert unparser.get_positional_args() == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([[1, 2, 3], [4, 5], [6]], [1, 2, 3, 4, 5, 6]),
        ([[["nested"]], [True]], [["nested"], True]),
    ]
)  # yapf: disable
def test__flatten_list(input_list, expected) -> None:
    assert ReverseArgumentParser._flatten_list(input_list) == expected


@pytest.fixture()
def parser() -> ArgumentParser:
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
        "--app-const1",
        dest="app_const",
        action="append_const",
        const=42
    )
    p.add_argument(
        "--app-const2",
        dest="app_const",
        action="append_const",
        const=53
    )
    p.add_argument("--verbose", "-v", action="count", default=2)
    p.add_argument("--ext", action="extend", nargs="*")
    p.add_argument("--bool-opt", action=BooleanOptionalAction, default=False)
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
]  # yapf: disable


@pytest.mark.parametrize("args", COMPLETE_ARGS)
def test_get_effective_command_line_invocation(parser, args) -> None:
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = (
        "__main__.py --opt1 opt1-val --opt2 opt2-val1 opt2-val2 --store-true "
        "--store-false --needs-quotes \'hello world\' --default 42 --app1 "
        "app1-val1 --app1 app1-val2 --app2 app2-val1 --app2 app2-val2 "
        "--app-nargs app-nargs1-val1 app-nargs1-val2 --app-nargs "
        "app-nargs2-val --const --app-const1 --app-const2 -vv --ext "
        "ext-val1 ext-val2 ext-val3 --no-bool-opt -- pos1-val1 pos1-val2 "
        "pos2-val"
    )
    assert unparser.get_effective_command_line_invocation() == expected


@pytest.mark.parametrize("args", COMPLETE_ARGS)
def test_get_pretty_command_line_invocation(parser, args) -> None:
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = """
__main__.py \\
    --opt1 opt1-val \\
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
    --ext ext-val1 ext-val2 ext-val3 \\
    --no-bool-opt \\
    -- \\
    pos1-val1 pos1-val2 \\
    pos2-val
""".strip()
    assert unparser.get_pretty_command_line_invocation() == expected


@pytest.mark.parametrize(
    "add_args, add_kwargs, args, expected",
    [(
        ["--foo"],
        {"action": "store"},
        "--foo bar",
        ["--foo", "bar"]
    ), (
        ["--foo"],
        {"action": "store_const", "const": 42},
        "--foo",
        ["--foo"]
    ), (
        ["--foo"],
        {"action": "store_true"},
        "--foo",
        ["--foo"]
    ), (
        ["--foo"],
        {"action": "store_false"},
        "--foo",
        ["--foo"]
    ), (
        ["--foo"],
        {"action": "append"},
        "--foo bar --foo baz",
        [["--foo", "bar"], ["--foo", "baz"]]
    ), (
        ["--foo"],
        {"dest": "append_const", "action": "append_const", "const": 42},
        "--foo",
        ["--foo"]
    ), (
        ["--foo", "-f"],
        {"action": "count", "default": 0},
        "--foo --foo",
        ["-ff"]
    ), (
        ["--foo"],
        {"action": "help"},
        "--foo",
        []
    ), (
        ["--foo"],
        {"action": "version", "version": "1.2.3"},
        "--foo",
        []
    ), (
        ["--foo"],
        {"action": "extend", "nargs": "*"},
        "--foo bar --foo baz bif",
        ["--foo", "bar", "baz", "bif"]
    ), (
        ["--foo"],
        {"action": BooleanOptionalAction},
        "--foo",
        ["--foo"]
    )]
)  # yapf: disable
def test__unparse_action(add_args, add_kwargs, args, expected) -> None:
    """
    Todo:  Add coverage for sub-parsers.
    """
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    try:
        namespace = parser.parse_args(shlex.split(args))
    except SystemExit:
        namespace = Namespace()
    unparser = ReverseArgumentParser(parser, namespace)
    if expected == "NotImplemented":
        with pytest.raises(NotImplementedError):
            unparser._unparse_action(action)
    else:
        assert unparser._unparse_action(action) == expected


@pytest.mark.parametrize(
    "strings, expected",
    [
        (["-v", "--verbose"], ["--verbose"]),
        (["--foo", "-f", "--foo-bar"], ["--foo", "--foo-bar"]),
        (["-x"], []),
    ]
)  # yapf: disable
def test__get_long_option_strings(strings, expected) -> None:
    unparser = ReverseArgumentParser(ArgumentParser(), Namespace())
    assert unparser._get_long_option_strings(strings) == expected


@pytest.mark.parametrize(
    "strings, expected",
    [
        (["-v", "--verbose"], ["-v"]),
        (["--foo", "-f", "--foo-bar"], ["-f"]),
        (["--foo"], []),
    ]
)  # yapf: disable
def test__get_short_option_strings(strings, expected) -> None:
    unparser = ReverseArgumentParser(ArgumentParser(), Namespace())
    assert unparser._get_short_option_strings(strings) == expected


@pytest.mark.parametrize(
    "strings, expected",
    [
        (["-v", "--verbose"], "--verbose"),
        (["--foo", "-f", "--foo-bar"], "--foo"),
        (["-x"], "-x"),
    ]
)  # yapf: disable
def test__get_option_string(strings, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(*strings)
    unparser = ReverseArgumentParser(parser, Namespace())
    assert unparser._get_option_string(action) == expected


@pytest.mark.parametrize(
    "strings, expected",
    [
        (["-v", "--verbose"], "-v"),
        (["-f", "--foo", "-b"], "-f"),
        (["--foo"], "--foo"),
    ]
)  # yapf: disable
def test__get_option_string_prefer_short(strings, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(*strings)
    unparser = ReverseArgumentParser(parser, Namespace())
    assert unparser._get_option_string(action, prefer_short=True) == expected


@pytest.mark.parametrize(
    "add_args, add_kwargs, args, expected",
    [(
        ["positional"],
        {},
        "val",
        ["val"]
    ), (
        ["-f", "--foo"],
        {},
        "-f bar",
        ["--foo", "bar"]
    ), (
        ["-f"],
        {},
        "-f bar",
        ["-f", "bar"]
    ), (
        ["--foo", "--foo-bar"],
        {},
        "--foo-bar baz",
        ["--foo", "baz"]
    ), (
        ["positional"],
        {"nargs": "*"},
        "val1 val2",
        ["val1", "val2"]
    ), (
        ["-f", "--foo"],
        {"nargs": "*"},
        "-f bar baz",
        ["--foo", "bar", "baz"]
    ), (
        ["-f"],
        {"nargs": "*"},
        "-f bar baz",
        ["-f", "bar", "baz"]
    ), (
        ["--foo", "--foo-bar"],
        {"nargs": "*"},
        "--foo-bar baz bif",
        ["--foo", "baz", "bif"]
    )]
)  # yapf: disable
def test__unparse_store_action(add_args, add_kwargs, args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_store_action(action) == expected


@pytest.mark.parametrize(
    "add_args, add_kwargs, args, expected",
    [(
        ["--foo"],
        {"action": "store_const", "const": 42},
        "",
        []
    ), (
        ["--foo"],
        {"action": "store_const", "const": 42},
        "--foo",
        ["--foo"]
    ), (
        ["--foo"],
        {"action": "store_const", "const": 42, "default": 53},
        "",
        []
    ), (
        ["--foo"],
        {"action": "store_const", "const": 42, "default": 53},
        "--foo",
        ["--foo"]
    )]
)  # yapf: disable
def test__unparse_store_const_action(
    add_args,
    add_kwargs,
    args,
    expected
) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_store_const_action(action) == expected


@pytest.mark.parametrize(
    "args, expected",
    [(shlex.split("--foo"), ["--foo"]), ([], [])]
)  # yapf: disable
def test__unparse_store_true_action(args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument("--foo", action="store_true")
    namespace = parser.parse_args(args)
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_store_true_action(action) == expected


@pytest.mark.parametrize(
    "args, expected",
    [(shlex.split("--foo"), ["--foo"]), ([], [])]
)  # yapf: disable
def test__unparse_store_false_action(args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument("--foo", action="store_false")
    namespace = parser.parse_args(args)
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_store_false_action(action) == expected


@pytest.mark.parametrize(
    "add_args, add_kwargs, args, expected",
    [(
        ["--foo"],
        {"action": "append"},
        "--foo bar --foo baz",
        [["--foo", "bar"], ["--foo", "baz"]]
    ), (
        ["--foo"],
        {"action": "append", "nargs": "*"},
        "--foo bar baz --foo bif",
        [["--foo", "bar", "baz"], ["--foo", "bif"]]
    )]
)  # yapf: disable
def test__unparse_append_action(add_args, add_kwargs, args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_append_action(action) == expected


@pytest.mark.parametrize(
    "args, expected",
    [("--foo", ["--foo"]), ("", [])]
)
def test__unparse_append_const_action(args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(
        "--foo",
        dest="append_const",
        action="append_const",
        const=42
    )
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_append_const_action(action) == expected


@pytest.mark.parametrize(
    "add_args, add_kwargs, args, expected",
    [(
        ["--foo"],
        {"action": "count"},
        "--foo --foo --foo",
        ["--foo", "--foo", "--foo"]
    ), (
        ["--verbose", "-v"],
        {"action": "count"},
        "--verbose -v --verbose",
        ["-vvv"]
    ), (
        ["--verbose", "-v"],
        {"action": "count", "default": 2},
        "-vv",
        ["-vv"]
    )]
)
def test__unparse_count_action(add_args, add_kwargs, args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(*add_args, **add_kwargs)
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_count_action(action) == expected


def test__unparse_sub_parsers_action() -> None:
    """
    Todo:  Figure out what to do about sub-parsers.
    """
    pass


def test__unparse_extend_action() -> None:
    parser = ArgumentParser()
    action = parser.add_argument("--foo", action="extend", nargs="*")
    namespace = parser.parse_args(shlex.split("--foo bar --foo baz bif"))
    unparser = ReverseArgumentParser(parser, namespace)
    expected = ["--foo", "bar", "baz", "bif"]
    assert unparser._unparse_extend_action(action) == expected


@pytest.mark.parametrize(
    "default, args, expected",
    [(
        None,
        "",
        []
    ), (
        None,
        "--bool-opt",
        ["--bool-opt"]
    ), (
        None,
        "--no-bool-opt",
        ["--no-bool-opt"]
    ), (
        True,
        "",
        ["--bool-opt"]
    ), (
        True,
        "--bool-opt",
        ["--bool-opt"]
    ), (
        True,
        "--no-bool-opt",
        ["--no-bool-opt"]
    ), (
        False,
        "",
        ["--no-bool-opt"]
    ), (
        False,
        "--bool-opt",
        ["--bool-opt"]
    ), (
        False,
        "--no-bool-opt",
        ["--no-bool-opt"]
    )]
)
def test__unparse_boolean_optional_action(default, args, expected) -> None:
    parser = ArgumentParser()
    action = parser.add_argument(
        "--bool-opt",
        action=BooleanOptionalAction,
        default=default
    )
    namespace = parser.parse_args(shlex.split(args))
    unparser = ReverseArgumentParser(parser, namespace)
    assert unparser._unparse_boolean_optional_action(action) == expected
