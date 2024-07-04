"""
The ``reverse_argparse`` module.

Defines the :class:`ReverseArgumentParser` class for unparsing arguments
that were already parsed via :mod:`argparse`, and the
:func:`quote_arg_if_necessary` helper function to surround any arguments
with spaces in them with quotes.
"""

# © 2023 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import re
import sys
from argparse import SUPPRESS, Action, ArgumentParser, Namespace
from typing import List, Sequence


BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION = 9
SHORT_OPTION_LENGTH = 2


class ReverseArgumentParser:
    """
    Argument parsing in reverse.

    Whereas :class:`argparse.ArgumentParser` is concerned with taking a
    bunch of command line arguments and parsing them into a
    :class:`argparse.Namespace`, this class is intended to do the
    opposite; that is, it'll take the parsed arguments and create the
    effective command line invocation of the script that generated them.
    The motivation is to be able to tell users exactly what was used for
    all of the options, taking into consideration any defaults and other
    transformations that might've been applied in the midst of parsing,
    such that they're able to reproduce a prior run of a script exactly.

    Attributes:
        _args (List[str]):  The list of arguments corresponding to each
            :class:`argparse.Action` in the given parser, which is built
            up as the arguments are unparsed.
        _indent (int):  The number of spaces with which to indent
            subsequent lines when pretty-printing the effective command
            line invocation.
        _namespace (Namespace):  The parsed arguments.
        _parsers (List[argparse.ArgumentParser]):  The parser that was
            used to generate the parsed arguments.  This is a ``list``
            (conceptually a stack) to allow for sub-parsers, so the
            outer-most parser is the first item in the list, and
            sub-parsers are pushed onto and popped off of the stack as
            they are processed.
        _unparsed (List[bool]):  A list in which the elements indicate
            whether the corresponding parser in :attr:`parsers` has been
            unparsed.
    """

    def __init__(
        self, parser: ArgumentParser, namespace: Namespace, indent: int = 4
    ):
        """
        Initialize the object.

        Args:
            parser:  The :class:`argparse.ArgumentParser` used to
                construct the given ``namespace``.
            namespace:  The parsed arguments.
            indent:  How many spaces to use for each indentation level.
                (See :func:`get_pretty_command_line_invocation`.)
        """
        self._unparsed = [False]
        self._args = [parser.prog]
        self._indent = indent
        self._parsers = [parser]
        self._namespace = namespace

    def _unparse_args(self) -> None:
        """
        Unparse all the arguments.

        Loop over the positional and then optional actions, generating
        the command line arguments associated with each, and appending
        them to the list of arguments.
        """
        if self._unparsed[-1]:
            return
        psr = self._parsers[-1]
        actions = (
            psr._get_optional_actions()  # pylint: disable=protected-access
            + psr._get_positional_actions()  # pylint: disable=protected-access
        )
        for action in actions:
            self._unparse_action(action)
        self._unparsed[-1] = True

    def _unparse_action(self, action: Action) -> None:  # noqa: C901, PLR0912
        """
        Unparse a single action.

        Generate the command line arguments associated with the given
        ``action``, and append them to the list of arguments.

        Args:
            action:  The :class:`argparse.Action` to unparse.

        Raises:
            NotImplementedError:  If there is not currently an
                implementation for unparsing the given action.
        """
        action_type = type(action).__name__
        if action_type != "_SubParsersAction" and (
            not hasattr(self._namespace, action.dest)
            or self._arg_is_default_and_help_is_suppressed(action)
        ):
            return
        if action_type == "_AppendAction":
            self._unparse_append_action(action)
        elif action_type == "_AppendConstAction":
            self._unparse_append_const_action(action)
        elif action_type == "_CountAction":
            self._unparse_count_action(action)
        elif action_type == "_ExtendAction":
            self._unparse_extend_action(action)
        elif action_type == "_HelpAction":  # pragma: no cover
            return
        elif action_type == "_StoreAction":
            self._unparse_store_action(action)
        elif action_type == "_StoreConstAction":
            self._unparse_store_const_action(action)
        elif action_type == "_StoreFalseAction":
            self._unparse_store_false_action(action)
        elif action_type == "_StoreTrueAction":
            self._unparse_store_true_action(action)
        elif action_type == "_SubParsersAction":
            self._unparse_sub_parsers_action(action)
        elif action_type == "_VersionAction":  # pragma: no cover
            return
        elif (
            action_type == "BooleanOptionalAction"
            and sys.version_info.minor >= BOOLEAN_OPTIONAL_ACTION_MINOR_VERSION
        ):
            self._unparse_boolean_optional_action(action)
        else:  # pragma: no cover
            message = (
                f"{self.__class__.__name__} does not yet support the "
                f"unparsing of {action_type} objects."
            )
            raise NotImplementedError(message)

    def _arg_is_default_and_help_is_suppressed(self, action: Action) -> bool:
        """
        See if the argument should be skipped.

        Determine whether the argument matches the default value and the
        corresponding help text has been suppressed.  Such cases
        indicate that a parser author has hidden an argument from users,
        and the user hasn't modified the value on the command line, so
        to match the author's intent, we should omit the argument from
        the effective command line invocation.

        Args:
            action:  The command line argument in question.

        Returns:
            ``True`` if the argument should be omitted; ``False``
            otherwise.
        """
        value = getattr(self._namespace, action.dest)
        return value == action.default and action.help == SUPPRESS

    def get_effective_command_line_invocation(self) -> str:
        """
        Get the effective command line invocation of a script.

        This takes into account what was passed into the script on the
        command line, along with any default values, etc., such that
        there is no ambiguity in what exactly was run.

        Returns:
            What you would need to run on the command line to reproduce
            what was run before.
        """
        self._unparse_args()
        return " ".join(_.strip() for _ in self._args if _.strip())

    def get_pretty_command_line_invocation(self) -> str:
        """
        Get a "pretty" version of the command that was run.

        Similar to :func:`get_effective_command_line_invocation`, but
        generate a string ready for "pretty-printing", with escaped
        newlines between each of the arguments, and appropriate
        indentation.

        Returns:
            What you would need to run on the command line to reproduce
            what was run before.
        """
        self._unparse_args()
        return " \\\n".join(_ for _ in self._args if _.strip())

    def _get_long_option_strings(
        self, option_strings: Sequence[str]
    ) -> List[str]:
        """
        Get the long options from a list of options strings.

        Args:
            option_strings:  The list of options strings.

        Returns:
            A list containing only the long options (e.g., ``"--foo"``),
            and not the short ones (e.g., ``"-f"``).  Note that the list
            will be empty if there are no long options.
        """
        return [
            option
            for option in option_strings
            if len(option) > SHORT_OPTION_LENGTH
            and option[0] in self._parsers[-1].prefix_chars
            and option[1] in self._parsers[-1].prefix_chars
        ]

    def _get_short_option_strings(
        self, option_strings: Sequence[str]
    ) -> List[str]:
        """
        Get the short options from a list of options strings.

        Args:
            option_strings:  The list of options strings.

        Returns:
            A list containing only the short options (e.g., ``"-f"``),
            and not the short ones (e.g., ``"--foo"``).  Note that the
            list will be empty if there are no short options.
        """
        return [
            option
            for option in option_strings
            if len(option) == SHORT_OPTION_LENGTH
            and option[0] in self._parsers[-1].prefix_chars
        ]

    def _get_option_string(
        self, action: Action, *, prefer_short: bool = False
    ) -> str:
        """
        Get the option string for the `action`.

        Get the first of the long options corresponding to a given
        :class:`argparse.Action`.  If no long options are available, get
        the first of the short options.  If ``prefer_short`` is
        ``True``, search the short options first, and fall back to the
        long ones if necessary.

        Args:
            action:  The :class:`argparse.Action` in question.
            prefer_short:  Whether to prefer the short options over the
                long ones.

        Returns:
            The option string, or the empty string, if no options string
            exists (e.g., for positional arguments).
        """
        short_options = self._get_short_option_strings(action.option_strings)
        long_options = self._get_long_option_strings(action.option_strings)
        if prefer_short:
            if short_options:
                return short_options[0]
            if long_options:
                return long_options[0]
        else:
            if long_options:
                return long_options[0]
            if short_options:
                return short_options[0]
        return ""

    def _append_list_of_list_of_args(self, args: List[List[str]]) -> None:
        """
        Append to the list of unparsed arguments.

        Given a list of lists of command line arguments corresponding to
        a particular action, append them to the list of arguments,
        taking into account indentation and the sub-parser nesting
        level.

        Args:
            args:  The command line arguments to be appended.
        """
        for line in args:
            self._args.append(self._indent_str + " ".join(line))

    def _append_list_of_args(self, args: List[str]) -> None:
        """
        Append to the list of unparsed arguments.

        Given a list of command line arguments corresponding to a
        particular action, append them to the list of arguments, taking
        into account indentation and the sub-parser nesting level.

        Args:
            args:  The command line arguments to be appended.
        """
        self._args.append(self._indent_str + " ".join(args))

    def _append_arg(self, arg: str) -> None:
        """
        Append to the list of unparsed arguments.

        Given a command line argument corresponding to a particular
        action, append it to the list of arguments, taking into account
        indentation and the sub-parser nesting level.

        Args:
            arg:  The command line argument to be appended.
        """
        self._args.append(self._indent_str + arg)

    @property
    def _indent_str(self) -> str:
        """
        The indentation level.

        Returns:
            A string of spaces corresponding to the indentation level.
        """
        return " " * self._indent * len(self._parsers)

    def _unparse_store_action(self, action: Action) -> None:
        """
        Generate the list of arguments for a ``store`` action.

        Args:
            action:  The :class:`_StoreAction` in question.
        """
        values = getattr(self._namespace, action.dest)
        if values is None:
            return
        flag = self._get_option_string(action)
        result = []
        if flag:
            result.append(flag)
        if not isinstance(values, list):
            values = [values]
        needs_quotes_regex = re.compile(r"(.*\s.*)")
        for value in values:
            string_value = str(value)
            if needs_quotes_regex.search(string_value):
                string_value = needs_quotes_regex.sub(r"'\1'", string_value)
            result.append(string_value)
        self._append_list_of_args(result)

    def _unparse_store_const_action(self, action: Action) -> None:
        """
        Generate the argument for a ``store_const`` action.

        Args:
            action:  The :class:`_StoreConstAction` in question.
        """
        value = getattr(self._namespace, action.dest)
        if value == action.const:
            self._append_arg(self._get_option_string(action))

    def _unparse_store_true_action(self, action: Action) -> None:
        """
        Generate the argument for a ``store_true`` action.

        Args:
            action:  The :class:`_StoreTrueAction` in question.
        """
        value = getattr(self._namespace, action.dest)
        if value is True:
            self._append_arg(self._get_option_string(action))

    def _unparse_store_false_action(self, action: Action) -> None:
        """
        Generate the argument for a ``store_false`` action.

        Args:
            action:  The :class:`_StoreFalseAction` in question.
        """
        value = getattr(self._namespace, action.dest)
        if value is False:
            self._append_arg(self._get_option_string(action))

    def _unparse_append_action(self, action: Action) -> None:
        """
        Generate the list of arguments for an ``append`` action.

        Args:
            action:  The :class:`_AppendAction` in question.
        """
        values = getattr(self._namespace, action.dest)
        if values is None:
            return
        flag = self._get_option_string(action)
        if not isinstance(values, list):
            values = [values]
        result = []
        if isinstance(values[0], list):
            for entry in values:
                tmp = [flag]
                for value in entry:
                    quoted_value = quote_arg_if_necessary(str(value))
                    tmp.append(quoted_value)
                result.append(tmp)
        else:
            for value in values:
                quoted_value = quote_arg_if_necessary(str(value))
                result.append([flag, quoted_value])
        self._append_list_of_list_of_args(result)

    def _unparse_append_const_action(self, action: Action) -> None:
        """
        Generate the argument for an ``append_const`` action.

        Args:
            action:  The :class:`_AppendConstAction` in question.
        """
        values = getattr(self._namespace, action.dest)
        if values is not None and action.const in values:
            self._append_arg(self._get_option_string(action))

    def _unparse_count_action(self, action: Action) -> None:
        """
        Generate the list of arguments for a ``count`` action.

        Args:
            action:  The :class:`_CountAction` in question.
        """
        value = getattr(self._namespace, action.dest)
        count = value if action.default is None else (value - action.default)
        flag = self._get_option_string(action, prefer_short=True)
        if (
            len(flag) == SHORT_OPTION_LENGTH
            and flag[0] in self._parsers[-1].prefix_chars
        ):
            self._append_arg(flag[0] + flag[1] * count)
        else:
            self._append_list_of_args([flag for _ in range(count)])

    def _unparse_sub_parsers_action(self, action: Action) -> None:
        """
        Generate the list of arguments for a subparser action.

        This is done by:

        * looping over the commands and corresponding parsers in the
          given subparser action,
        * recursively unparsing the subparser, and
        * if the subparser wasn't used to parse the command line
          arguments, removing it before continuing with the next
          subcommand-subparser pair.

        Args:
            action:  The :class:`_SubParsersAction` in question.

        Raises:
            RuntimeError:  If a subparser action is somehow missing its
                dictionary of choices.
        """
        if action.choices is None or not isinstance(
            action.choices, dict
        ):  # pragma: no cover
            message = (
                "This subparser action is missing its dictionary of "
                f"choices:  {action}"
            )
            raise RuntimeError(message)
        for subcommand, subparser in action.choices.items():
            self._parsers.append(subparser)
            self._unparsed.append(False)
            self._args.append(
                " " * self._indent * (len(self._parsers) - 1) + subcommand
            )
            args_before = self._args.copy()
            self._unparse_args()
            if self._args == args_before:
                self._parsers.pop()
                self._unparsed.pop()
                self._args.pop()

    def _unparse_extend_action(self, action: Action) -> None:
        """
        Generate the list of arguments for an ``extend`` action.

        Args:
            action:  The :class:`_ExtendAction` in question.
        """
        values = getattr(self._namespace, action.dest)
        if values is not None:
            self._append_list_of_args(
                [self._get_option_string(action), *values]
            )

    def _unparse_boolean_optional_action(self, action: Action) -> None:
        """
        Generate the list of arguments for a ``BooleanOptionalAction``.

        Args:
            action:  The :class:`BooleanOptionalAction` in question.
        """
        value = getattr(self._namespace, action.dest)
        if value is not None:
            flag_index = 0 if getattr(self._namespace, action.dest) else 1
            self._append_arg(action.option_strings[flag_index])


def quote_arg_if_necessary(arg: str) -> str:
    """
    Quote an argument, if necessary.

    If a command line argument has any spaces in it, surround it in
    single quotes.  If no quotes are necessary, don't change the
    argument.

    Args:
        arg:  The command line argument.

    Returns:
        The (possibly) quoted argument.
    """
    needs_quotes_regex = re.compile(r"(.*\s.*)")
    if needs_quotes_regex.search(arg):
        return needs_quotes_regex.sub(r"'\1'", arg)
    return arg
