
from .program_name import get_program_name

import os
import sys

_STDERR_ISATTY = sys.stderr.isatty()
_OS_IS_POSIX = os.name.lower() == 'posix'

STOCK_TRAILING_PROMPT = 'use --help for usage'
"""The trailing prompt used when trailing_prompt=True is passed to abort() (and family) and no default trailing prompt has been set (via set_default_trailing_prompt())"""

_trailing_prompt = None

def set_default_trailing_prompt(prompt):
    """Sets the default trailing prompt.

    Parameters
    ----------
    prompt : string
        The new default trailing prompt

    Returns
    -------
        The previous default trailing prompt

    Notes
    -----
        This method is NOT threadsafe, so in a multithreaded context the set prompt and/or the return value may not be as expected
"""

    global _trailing_prompt

    _trailing_prompt, prompt = prompt, _trailing_prompt

    return prompt


def _emit_to_cr_stm(message):

    sys.stderr.write(message)


def _add_eol_and_emit_to_cr_stm(message):

    _emit_to_cr_stm(message + "\n")


def _isatty():

    return _STDERR_ISATTY and _OS_IS_POSIX


def conrep(message, **kwargs):
    """DEPRECATED: use report()."""

    return report(message, **kwargs)


def report(message, show_program_name=True):
    """Emits the given message (and optional prefix) on the contingent report stream.

    Parameters
    ----------
    message : str
        The (main body of the) message to be displayed, which is optionally prefixed by program-name + ': '

    show_program_name : bool, optional
        Prevents the default prefixing of the message with program-name + ': ' if False. Default is True
"""

    if show_program_name:

        pn = get_program_name()

        _emit_to_cr_stm(pn + ": " + str(message) + "\n")
    else:

        _add_eol_and_emit_to_cr_stm(message)


def abort(message, do_exit=True, show_program_name=True, trailing_prompt=None):
    """Emits the given message (and optional prefix and suffix) on the contingent report stream, and then terminates the process

    Parameters
    ----------
    message : str
        The (main body of the) message to be displayed, which is optionally prefixed by program-name + ': ' and optionally suffixed by '; ' + trailing-prompt

    do_exit : bool, optional
        Prevents default behaviour of a call to sys.exit(1) (after printing the abort message) if False. Default is True

    show_program_name : bool, optional
        Prevents the default prefixing of the message with program-name + ': ' if False. Default is True

    trailing_prompt : str, bool, optional
        Affects the use of the trailing prompt as follows: if False, no trailing prompt is shown; if a (non-empty) string, that is used; if None, the default trailing prompt, if any, is used; if True, the default trailing prompt is used if specified, otherwise the STOCK_TRAILING_PROMPT is used
"""

    if False:

        pass
    elif False == trailing_prompt:

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

        if not trailing_prompt:

            trailing_prompt = False

    if trailing_prompt:

        message = message + '; ' + trailing_prompt

    report(message, show_program_name=show_program_name)

    if do_exit:

        sys.exit(1)


def warn(message):
    """Analogue of Ruby's Kernel#warn()

    Parameters
    ----------
        message : str, None
        The message to be emitted to the standard error stream (along with a new-line sequence). If None, nothing is emitted
    """

    if message:

        _add_eol_and_emit_to_cr_stm(message)

