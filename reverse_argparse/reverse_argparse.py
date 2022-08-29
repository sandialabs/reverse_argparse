#!/usr/bin/env python3

import re
from argparse import Action, ArgumentParser, Namespace
from typing import Any


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
        parser:  The :class:`argparse.ArgumentParser` that was used to
            generate the parsed arguments.
        namespace:  The :class:`argparse.Namespace` containing the
            parsed arguments.
    """

    def __init__(self, parser: ArgumentParser, namespace: Namespace):
        self.parser = parser
        self.namespace = namespace

    def _get_args(self, actions: list[Action]) -> list[list[str]]:
        """
        Get the arguments associated with each argument in the given
        list of actions.

        Args:
            actions:  The actions in question.

        Returns:
            A list of lists, where each element of the outer list
            corresponds to an :class:`Action`, and each inner list
            represents the command line arguments that generate the
            :class:`Action`.
        """
        result = []
        for action in actions:
            if arg := self._unparse_action(action):
                if type(arg) is list and type(arg[0]) is list:
                    result.extend(arg)
                else:
                    result.append(arg)
        return result

    def get_optional_args(self) -> list[list[str]]:
        """
        Get all the optional arguments.

        Returns:
            A list of lists, where each element of the outer list
            corresponds to an :class:`Action`, and each inner list
            represents the command line arguments that generate the
            :class:`Action`.
        """
        return self._get_args(self.parser._get_optional_actions())

    def get_positional_args(self) -> list[list[str]]:
        """
        Get all the positional arguments.

        Returns:
            A list of lists, where each element of the outer list
            corresponds to an :class:`Action`, and each inner list
            represents the command line arguments that generate the
            :class:`Action`.
        """
        return self._get_args(self.parser._get_positional_actions())

    @staticmethod
    def _flatten_list(list_of_lists: list[list[Any]]) -> list[Any]:
        """
        Flatten a list of lists.  E.g.,

            [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

        becomes

            [1, 2, 3, 4, 5, 6, 7, 8, 9]

        Args:
            list_of_lists:  The input list of lists.

        Returns:
            The list resulting from the flattening.

        Note:
            This only flattens the top two layers.  If an inner list
            also contains a list, it will not be flattened recursively.
        """
        return [item for sublist in list_of_lists for item in sublist]

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
        command_line = (
            f"{self.parser.prog} "
            + " ".join(self._flatten_list(self.get_optional_args()))
        )
        if positional_args := self.get_positional_args():
            command_line += (" -- "
                             + " ".join(self._flatten_list(positional_args)))
        return command_line

    def get_pretty_command_line_invocation(self, indent: int = 4) -> str:
        """
        Similar to :func:`get_effective_command_line_invocation`, but
        generate a string ready for "pretty-printing", with escaped
        newlines between each of the arguments.

        Args:
            indent:  How many spaces to indent each subsequent line.

        Returns:
            What you would need to run on the command line to reproduce
            what was run before.
        """
        indent_str = " " * indent
        command_line = self.parser.prog
        for action_args in self.get_optional_args():
            command_line += f" \\\n{indent_str}" + " ".join(action_args)
        if positional_args := self.get_positional_args():
            command_line += f" \\\n{indent_str}--"
        for action_args in positional_args:
            command_line += f" \\\n{indent_str}" + " ".join(action_args)
        return command_line

    def _unparse_action(self, action: Action) -> list[str] | list[list[str]]:
        """
        Given an action, generate the list of command line arguments
        that correspond to it.

        Args:
            action:  The action to be "un-parsed".

        Raises:
            NotImplementedError:  If there is not currently an
                implementation for "un-parsing" the given action.

        Returns:
            The list of command line arguments.
        """
        match type(action).__name__:
            case "_StoreAction":
                return self._unparse_store_action(action)
            case "_StoreConstAction":
                return self._unparse_store_const_action(action)
            case "_StoreTrueAction":
                return self._unparse_store_true_action(action)
            case "_StoreFalseAction":
                return self._unparse_store_false_action(action)
            case "_AppendAction":
                return self._unparse_append_action(action)
            case "_AppendConstAction":
                return self._unparse_append_const_action(action)
            case "_CountAction":
                return self._unparse_count_action(action)
            case "_HelpAction":
                return []
            case "_VersionAction":
                return []
            case "_SubParsersAction":
                return self._unparse_sub_parsers_action(action)
            case "_ExtendAction":
                return self._unparse_extend_action(action)
            case "BooleanOptionalAction":
                return self._unparse_boolean_optional_action(action)
            case _:
                raise NotImplementedError(
                    f"{__class__.__name__} does not yet support the "
                    f"un-parsing of {type(action).__name__} objects."
                )

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
                and option[0] in self.parser.prefix_chars
                and option[1] in self.parser.prefix_chars]

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
                and option[0] in self.parser.prefix_chars]

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

    @staticmethod
    def _quote_arg_if_necessary(arg: str) -> str:
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

    def _unparse_store_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="store"``.

        Args:
            action:  The :class:`_StoreAction` in question.

        Returns:
            The associated list of arguments.
        """
        values = getattr(self.namespace, action.dest)
        if values is None:
            return []
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
        return result

    def _unparse_store_const_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="store_const"``.

        Args:
            action:  The :class:`_StoreConstAction` in question.

        Returns:
            The associated list of arguments.
        """
        value = getattr(self.namespace, action.dest)
        return ([self._get_option_string(action)]
                if value == action.const else [])

    def _unparse_store_true_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="store_true"``.

        Args:
            action:  The :class:`_StoreTrueAction` in question.

        Returns:
            The associated list of arguments.
        """
        value = getattr(self.namespace, action.dest)
        return [self._get_option_string(action)] if value is True else []

    def _unparse_store_false_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="store_false"``.

        Args:
            action:  The :class:`_StoreFalseAction` in question.

        Returns:
            The associated list of arguments.
        """
        value = getattr(self.namespace, action.dest)
        return [self._get_option_string(action)] if value is False else []

    def _unparse_append_action(self, action: Action) -> list[list[str]]:
        """
        Generate the list of arguments that correspond to
        ``action="append"``.

        Args:
            action:  The :class:`_AppendAction` in question.

        Returns:
            The associated list of arguments, broken up into sub-lists,
            one per flag.
        """
        values = getattr(self.namespace, action.dest)
        if values is None:
            return []
        flag = self._get_option_string(action)
        if type(values) is not list:
            values = [values]
        result = []
        if type(values[0]) is list:
            for entry in values:
                tmp = [flag]
                for value in entry:
                    value = self._quote_arg_if_necessary(str(value))
                    tmp.append(value)
                result.append(tmp)
        else:
            for value in values:
                value = self._quote_arg_if_necessary(str(value))
                result.append([flag, value])
        return result

    def _unparse_append_const_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="append_const"``.

        Args:
            action:  The :class:`_AppendConstAction` in question.

        Returns:
            The associated list of arguments.
        """
        values = getattr(self.namespace, action.dest)
        return ([] if values is None or action.const not in values
                else [self._get_option_string(action)])

    def _unparse_count_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="count"``.

        Args:
            action:  The :class:`_CountAction` in question.

        Returns:
            The associated list of arguments.
        """
        value = getattr(self.namespace, action.dest)
        count = value if action.default is None else (value - action.default)
        flag = self._get_option_string(action, prefer_short=True)
        if len(flag) == 2 and flag[0] in self.parser.prefix_chars:
            return [flag[0] + flag[1] * count]
        else:
            return [flag for _ in range(count)]

    def _unparse_sub_parsers_action(self, action: Action) -> list[str]:
        raise NotImplementedError

    def _unparse_extend_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action="extend"``.

        Args:
            action:  The :class:`_ExtendAction` in question.

        Returns:
            The associated list of arguments.
        """
        values = getattr(self.namespace, action.dest)
        return ([] if values is None
                else [self._get_option_string(action)] + values)

    def _unparse_boolean_optional_action(self, action: Action) -> list[str]:
        """
        Generate the list of arguments that correspond to
        ``action=BooleanOptionalAction``.

        Args:
            action:  The :class:`BooleanOptionalAction` in question.

        Returns:
            The associated list of arguments.
        """
        value = getattr(self.namespace, action.dest)
        flag_index = 0 if getattr(self.namespace, action.dest) else 1
        return [] if value is None else [action.option_strings[flag_index]]
