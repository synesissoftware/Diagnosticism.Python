
from .program_name import get_program_name

from .internal import (
    _is_python_2_7_or_later,
    _is_windows_11_or_later,
)

import os
import sys


def _supports_ansi_sequences():

    if os.name.lower() == 'posix':

        return True

    if _is_windows_11_or_later():

        return True

    return False


_OS_IS_POSIX = _supports_ansi_sequences()

STOCK_TRAILING_PROMPT = 'use --help for usage'
"""The trailing prompt used when trailing_prompt=True is passed to abort() (and family) and no default trailing prompt has been set (via set_default_trailing_prompt())"""

_trailing_prompt = None


def set_default_trailing_prompt(prompt):
    """
    Sets the default trailing prompt.

    Parameters
    ----------
    prompt : str
        The new default trailing prompt

    Returns
    -------
    str
        The previous default trailing prompt

    Notes
    -----
        This method is NOT threadsafe, so in a multithreaded context the set prompt and/or the return value may not be as expected
    """

    global _trailing_prompt

    _trailing_prompt, prompt = prompt, _trailing_prompt

    return prompt


def _emit_to_cr_stm(
    file,
    message,
):
    assert file

    file.write(message)


def _get_cr_file_or_default(file):

    if file:

        return file

    return sys.stderr


def _add_eol_and_emit_to_cr_stm(
    file,
    message,
):

    _emit_to_cr_stm(
        file,
        message + "\n",
    )


def _isatty(
    file,
):

    if not _OS_IS_POSIX:

        return False

    file = _get_cr_file_or_default(file)

    if not file.isatty():

        return False

    return True


def _do_report(
    file,
    message,
    program_name,
    trailing_prompt,
):
    assert file

    # first process trailing prompt (as more complex)

    if False != trailing_prompt:

        if False:

            pass
        elif True == trailing_prompt:

            dtp = _trailing_prompt

            if dtp:

                trailing_prompt = dtp
            else:

                trailing_prompt = STOCK_TRAILING_PROMPT
        elif None == trailing_prompt:

            dtp = _trailing_prompt

            if dtp:

                trailing_prompt = dtp
        else:

            trailing_prompt = str(trailing_prompt)

            #trailing_prompt = trailing_prompt.strip()

            if not trailing_prompt:

                trailing_prompt = False

    if program_name:

        if True == program_name:

            program_name = get_program_name()

    if program_name:

        if trailing_prompt:

            # TODO: perf test this
            _emit_to_cr_stm(file, program_name + ": " + str(message) + '; ' + trailing_prompt + "\n")
        else:

            # TODO: perf test this
            _emit_to_cr_stm(file, program_name + ": " + str(message) + "\n")
    else:

        if trailing_prompt:

            # TODO: perf test this
            _emit_to_cr_stm(file, message + '; ' + trailing_prompt + "\n")
        else:

            _add_eol_and_emit_to_cr_stm(file, message)


if _is_python_2_7_or_later():

    def conrep(
        message,
        **kwargs,
    ):
        """
        DEPRECATED: use `report()`.
        """

        show_program_name = kwargs.get('show_program_name', True)

        return report(
            message,
            show_program_name=show_program_name,
        )


def report(
    message,
    show_program_name=True,
    file=None,
):
    """
    Emits the given message (and optional prefix) on the contingent report stream.

    Parameters
    ----------
    message : str
        The (main body of the) message to be displayed, which is optionally prefixed by program-name + ': '

    show_program_name : bool, optional
        Prevents the default prefixing of the message with program-name + ': ' if `False`. Default is `True`
    """

    trailing_prompt = False

    file = _get_cr_file_or_default(file)

    _do_report(
        file,
        message,
        show_program_name,
        trailing_prompt,
    )


def abort(
    message,
    do_exit=True,
    show_program_name=True,
    trailing_prompt=None,
    file=None,
):
    """
    Emits the given message (and optional prefix and suffix) on the contingent report stream, and then terminates the process

    Parameters
    ----------
    message : str
        The (main body of the) message to be displayed, which is optionally prefixed by program-name + ': ' and optionally suffixed by '; ' + trailing-prompt

    do_exit : bool, optional
        Prevents default behaviour of a call to `sys.exit(1)` (after printing the abort message) if `False`. Default is `True`

    show_program_name : bool, optional
        Prevents the default prefixing of the message with program-name + ': ' if `False`. Default is `True`

    trailing_prompt : str, bool, optional
        Affects the use of the trailing prompt as follows: if `False`, no trailing prompt is shown; if a (non-empty) string, that is used; if `None`, the default trailing prompt, if any, is used; if `True`, the default trailing prompt is used if specified, otherwise `STOCK_TRAILING_PROMPT` is used
    """

    file = _get_cr_file_or_default(file)

    _do_report(
        file,
        message,
        show_program_name,
        trailing_prompt,
    )

    if do_exit:

        sys.exit(1)


# ############################## end of file ############################# #

