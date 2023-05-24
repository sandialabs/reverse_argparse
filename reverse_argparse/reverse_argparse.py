#!/usr/bin/env python3

import re
from argparse import Action, ArgumentParser, Namespace, SUPPRESS


class ReverseArgumentParser:
    """
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
        _unparsed (list[bool]):  A list in which the elements indicate
            whether the corresponding parser in :attr:`parsers` has been
            unparsed.
        args (list[str]):  The list of arguments corresponding to each
            :class:`Action` in the given parser, which is built up as
            the arguments are unparsed.
        indent (int):  The number of spaces with which to indent
            subsequent lines when pretty-printing the effective command
            line invocation.
        parsers (list[ArgumentParser]):  The parser that was used to
            generate the parsed arguments.  This is a ``list``
            (conceptually a stack) to allow for sub-parsers, so the
            outer-most parser is the first item in the list, and
            sub-parsers are pushed onto and popped off of the stack as
            they are processed.
        namespace (Namespace):  The parsed arguments.
    """

    def __init__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        indent: int = 4
    ):
        self._unparsed = [False]
        self.args = [parser.prog]
        self.indent = indent
        self.parsers = [parser]
        self.namespace = namespace

    def _unparse_args(self) -> None:
        """
        Loop over the positional and then optional actions, generating
        the command line arguments associated with each, and appending
        them to the list of arguments.

        Raises:
            NotImplementedError:  If there is not currently an
                implementation for unparsing the given action.
        """
        if self._unparsed[-1]:
            return
        actions = (self.parsers[-1]._get_optional_actions()
                   + self.parsers[-1]._get_positional_actions())
        for action in actions:
            if (type(action).__name__ != "_SubParsersAction"
                and (not hasattr(self.namespace, action.dest)
                     or self._arg_is_default_and_help_is_suppressed(action))):
                continue
            match type(action).__name__:
                case "_AppendAction":
                    self._unparse_append_action(action)
                case "_AppendConstAction":
                    self._unparse_append_const_action(action)
                case "_CountAction":
                    self._unparse_count_action(action)
                case "_ExtendAction":
                    self._unparse_extend_action(action)
                case "_HelpAction":
                    continue
                case "_StoreAction":
                    self._unparse_store_action(action)
                case "_StoreConstAction":
                    self._unparse_store_const_action(action)
                case "_StoreFalseAction":
                    self._unparse_store_false_action(action)
                case "_StoreTrueAction":
                    self._unparse_store_true_action(action)
                case "_SubParsersAction":
                    self._unparse_sub_parsers_action(action)
                case "_VersionAction":
                    continue
                case "BooleanOptionalAction":
                    self._unparse_boolean_optional_action(action)
                case _:
                    raise NotImplementedError(
                        f"{__class__.__name__} does not yet support the "
                        f"unparsing of {type(action).__name__} objects."
                    )
        self._unparsed[-1] = True

    def _arg_is_default_and_help_is_suppressed(self, action: Action) -> bool:
        """
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
        value = getattr(self.namespace, action.dest)
        return value == action.default and action.help == SUPPRESS

    def get_effective_command_line_invocation(self) -> str:
        """
        Get the effective command line invocation of a script.  This
        takes into account what was passed into the script on the
        command line, along with any default values, etc., such that
        there is no ambiguity in what exactly was run.

        Returns:
            What you would need to run on the command line to reproduce
            what was run before.
        """
        self._unparse_args()
        return " ".join(_.strip() for _ in self.args if _.strip())

    def get_pretty_command_line_invocation(self) -> str:
        """
        Similar to :func:`get_effective_command_line_invocation`, but
        generate a string ready for "pretty-printing", with escaped
        newlines between each of the arguments.

        Returns:
            What you would need to run on the command line to reproduce
            what was run before.
        """
        self._unparse_args()
        return " \\\n".join(_ for _ in self.args if _.strip())

    def _get_long_option_strings(
        self,
        option_strings: list[str]
    ) -> list[str]:
        """
        Get the long options from a list of options strings.

        Args:
            option_strings:  The list of options strings.

        Returns:
            A list containing only the long options (e.g., ``"--foo"``),
            and not the short ones (e.g., ``"-f"``).  Note that the list
            will be empty if there are no long options.
        """
        return [option for option in option_strings
                if len(option) > 2
                and option[0] in self.parsers[-1].prefix_chars
                and option[1] in self.parsers[-1].prefix_chars]

    def _get_short_option_strings(
        self,
        option_strings: list[str]
    ) -> list[str]:
        """
        Get the short options from a list of options strings.

        Args:
            option_strings:  The list of options strings.

        Returns:
            A list containing only the short options (e.g., ``"-f"``),
            and not the short ones (e.g., ``"--foo"``).  Note that the
            list will be empty if there are no short options.
        """
        return [option for option in option_strings
                if len(option) == 2
                and option[0] in self.parsers[-1].prefix_chars]

    def _get_option_string(
        self,
        action: Action,
        prefer_short: bool = False
    ) -> str:
        """
        Get the first of the long options corresponding to a given
        :class:`Action`.  If no long options are available, get the
        first of the short options.  If :arg:`prefer_short` is ``True``,
        search the short options first, and fall back to the long ones
        if necessary.

        Args:
            action:  The :class:`Action` in question.
            prefer_short:  Whether to prefer the short options over the
                long ones.

        Returns:
            The option string.
        """
        short_options = self._get_short_option_strings(action.option_strings)
        long_options = self._get_long_option_strings(action.option_strings)
        if prefer_short:
            if short_options:
                return short_options[0]
            elif long_options:
                return long_options[0]
        else:
            if long_options:
                return long_options[0]
            elif short_options:
                return short_options[0]

    def _append(self, args: list[str] | list[list[str]]) -> None:
        """
        Given a list of command line arguments corresponding to a
        particular action, append them to the list of arguments, taking
        into account indentation and the sub-parser nesting level.

        Args:
            args:  The command line arguments to be appended.
        """
        indent_str = " " * self.indent * len(self.parsers)
        if type(args) is list and len(args) > 0 and type(args[0]) is list:
            for line in args:
                self.args.append(indent_str + " ".join(line))
        else:
            self.args.append(indent_str + " ".join(args))

    def _unparse_store_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="store"``.

        Args:
            action:  The :class:`_StoreAction` in question.
        """
        values = getattr(self.namespace, action.dest)
        if values is None:
            return
        flag = self._get_option_string(action)
        result = []
        if flag:
            result += [flag]
        if type(values) is not list:
            values = [values]
        for i in range(len(values)):
            needs_quotes_regex = re.compile(r"(.*\s.*)")
            values[i] = str(values[i])
            if needs_quotes_regex.search(values[i]):
                values[i] = needs_quotes_regex.sub(r"'\1'", values[i])
        result.extend(values)
        self._append(result)

    def _unparse_store_const_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="store_const"``.

        Args:
            action:  The :class:`_StoreConstAction` in question.
        """
        value = getattr(self.namespace, action.dest)
        self._append(
            [self._get_option_string(action)] if value == action.const else []
        )

    def _unparse_store_true_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="store_true"``.

        Args:
            action:  The :class:`_StoreTrueAction` in question.
        """
        value = getattr(self.namespace, action.dest)
        self._append(
            [self._get_option_string(action)] if value is True else []
        )

    def _unparse_store_false_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="store_false"``.

        Args:
            action:  The :class:`_StoreFalseAction` in question.
        """
        value = getattr(self.namespace, action.dest)
        self._append(
            [self._get_option_string(action)] if value is False else []
        )

    def _unparse_append_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="append"``.

        Args:
            action:  The :class:`_AppendAction` in question.
        """
        values = getattr(self.namespace, action.dest)
        if values is None:
            return
        flag = self._get_option_string(action)
        if type(values) is not list:
            values = [values]
        result = []
        if type(values[0]) is list:
            for entry in values:
                tmp = [flag]
                for value in entry:
                    value = quote_arg_if_necessary(str(value))
                    tmp.append(value)
                result.append(tmp)
        else:
            for value in values:
                value = quote_arg_if_necessary(str(value))
                result.append([flag, value])
        self._append(result)

    def _unparse_append_const_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="append_const"``.

        Args:
            action:  The :class:`_AppendConstAction` in question.
        """
        values = getattr(self.namespace, action.dest)
        self._append(
            [] if values is None or action.const not in values
            else [self._get_option_string(action)]
        )

    def _unparse_count_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="count"``.

        Args:
            action:  The :class:`_CountAction` in question.
        """
        value = getattr(self.namespace, action.dest)
        count = value if action.default is None else (value - action.default)
        flag = self._get_option_string(action, prefer_short=True)
        if len(flag) == 2 and flag[0] in self.parsers[-1].prefix_chars:
            self._append([flag[0] + flag[1] * count])
        else:
            self._append([flag for _ in range(count)])

    def _unparse_sub_parsers_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to a subparser
        action.  This is done by:

        * looping over the commands and corresponding parsers in the
          given subparser action,
        * recursively unparsing the subparser, and
        * if the subparser wasn't used to parse the command line
          arguments, removing it before continuing with the next
          subcommand-subparser pair.

        Args:
            action:  The :class:`_SubParsersAction` in question.
        """
        for subcommand, subparser in action.choices.items():
            self.parsers.append(subparser)
            self._unparsed.append(False)
            self.args.append(
                " " * self.indent * (len(self.parsers) - 1) + subcommand
            )
            args_before = self.args.copy()
            self._unparse_args()
            if self.args == args_before:
                self.parsers.pop()
                self._unparsed.pop()
                self.args.pop()

    def _unparse_extend_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action="extend"``.

        Args:
            action:  The :class:`_ExtendAction` in question.
        """
        values = getattr(self.namespace, action.dest)
        self._append(
            [] if values is None
            else [self._get_option_string(action)] + values
        )

    def _unparse_boolean_optional_action(self, action: Action) -> None:
        """
        Generate the list of arguments that correspond to
        ``action=BooleanOptionalAction``.

        Args:
            action:  The :class:`BooleanOptionalAction` in question.
        """
        value = getattr(self.namespace, action.dest)
        flag_index = 0 if getattr(self.namespace, action.dest) else 1
        self._append(
            [] if value is None else [action.option_strings[flag_index]]
        )


def quote_arg_if_necessary(arg: str) -> str:
    """
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
    else:
        return arg
