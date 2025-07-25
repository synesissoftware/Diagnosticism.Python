
from .contingent_reporting import (
    _do_report,
    _get_cr_file_or_default,
    _isatty,
)
from .program_name import get_program_name
from . import severity as _severity

from .internal import (
    _bool_from_env,
)

from datetime import datetime as dt
import sys
import threading


_REAL_STDERR = sys.stderr

def _get_stderr_dynamic():

    return sys.stderr

def _get_stderr_static():

    return _REAL_STDERR


def _get_log_file_or_default(file):

    if file:

        return file

    return _get_stderr_dynamic()


class _clrs:

    RED         =   "\x1B[31m"
    GREEN       =   "\x1B[32m"
    YELLOW      =   "\x1B[33m"
    BLUE        =   "\x1B[34m"
    MAGENTA     =   "\x1B[35m"
    DARKGREY    =   "\x1B[90m"
    NONE        =   "\x1B[0m"

    D   =   {

        _severity.VIOLATION         :   RED,
        _severity.ALERT             :   RED,
        _severity.CRITICAL          :   RED,
        _severity.FAILURE           :   RED,
        _severity.WARNING           :   YELLOW,
        _severity.NOTICE            :   MAGENTA,
        _severity.INFORMATIONAL     :   MAGENTA,
        _severity.DEBUG0            :   BLUE,
        _severity.DEBUG1            :   BLUE,
        _severity.DEBUG2            :   BLUE,
        _severity.DEBUG3            :   BLUE,
        _severity.DEBUG4            :   BLUE,
        _severity.DEBUG5            :   BLUE,
        _severity.TRACE             :   DARKGREY,
        _severity.BENCHMARK         :   DARKGREY,
    }


# ######################################
# Runtime shared state

_logging_is_enabled =   None
_log_filter         =   None
_others_action      =   None


def enable_logging(*args):
    """
    Enables/disables logging.

    Parameters
    ----------
    *args
        1 or 2 arguments: if 1, then is a `bool` determining whether should be enabled; if 2, then first is name(s) of environment variable(s) to be parsed and second is a `bool` specifying the default if not found in the environment

    Returns
    -------
    bool
        The previous enable/disable setting

    Raises
    ------
    ValueError
        If the string form of `v` does not contain a recognisable severity level
    """

    is_enabled = _bool_from_env(args, 'enable_logging')

    assert(is_enabled == True or is_enabled == False or is_enabled is None)

    global _logging_is_enabled

    _logging_is_enabled, is_enabled = is_enabled, _logging_is_enabled

    return is_enabled


def is_logging_enabled():
    """
    Indicate whether logging is enabled
    """

    return _logging_is_enabled


def is_severity_logged(severity):
    """
    Indicates whether the given severity is logged

    Returns
    -------
    bool
        `True` if the severity is to be logged; `False` otherwise
    """

    if not _logging_is_enabled:

        return False

    if _log_filter:

        if isinstance(_log_filter, (dict, )):

            r = _log_filter.get(severity, _others_action)

            if not r:

                return False
        else:

            if int(severity) > int(_log_filter):

                return False

    return True


def set_log_filter(
    log_filter,
    others_action=None,
):
    """
    Sets a logging filter, which may either specify a threshold severity or a mapping of levels to actions

    Parameters
    ----------
    log_filter : int, dict
        If a dictionary, it is interpreted as a mapping from severity-level to `True`/`False` that controls each level's output; otherwise, treated as a severity-level threshold (and must be convertible to `int`)

    others_action : obj, optional
        An object to be passed to be used in the case that the log_filter is a dictionary and the severity is not recognised

    Returns
    -------
    tuple
        Tuple of the previous (log_filter, others_action) value(s)
    """

    assert log_filter is None or isinstance(log_filter, (dict, )) or isinstance(int(log_filter), int)

    global _log_filter, _others_action

    _log_filter, log_filter, _others_action, others_action = log_filter, _log_filter, others_action, _others_action

    return (log_filter, others_action)


def _do_log(
    file,
    severity,
    message,
):
    """
    INTERNAL FUNCTION ONLY
    """

    assert file

    now = dt.now()

    ss = _severity.severity_to_string(severity)

    if _isatty(file):

        r = _clrs.D.get(severity, None)

        if r:

            ss = r + ss + _clrs.NONE

    # TODO: perf test this
    prefix = "[%s, %s, %s, %s]" % (get_program_name(), threading.current_thread().ident, str(now), ss)

    if hasattr(message, '__call__'):
        message = message()

    # TODO: perf test this
    full = prefix + ': ' + message

    show_program_name = False
    trailing_prompt = False

    file = _get_cr_file_or_default(file)

    _do_report(
        file,
        full,
        show_program_name,
        trailing_prompt,
    )


def log(
    severity,
    message,
    file=None,
):
    """
    Conditionally issue the given log message based on the given severity

    Parameters
    ----------
    severity : int
        The severity associated with the message

    message : str, callable
        A message string to be emitted, or a callable object that will yield an emittable string when called

    Returns
    -------
    None
    """

    if not is_severity_logged(severity):

        return

    file = _get_log_file_or_default(file)

    return _do_log(
        file,
        severity,
        message,
    )


# ############################## end of file ############################# #

