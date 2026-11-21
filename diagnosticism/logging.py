
from __future__ import absolute_import

from .contingent_reporting import (
    _do_report,
    _get_cr_file_or_default,
    _isatty,
    _output_lock,
)
from .program_name import get_program_name
from . import severity as _severity

from .internal import (
    _bool_from_env,
    _bool_from_named_env,
)

from datetime import datetime as dt
import logging as stdlib_logging
import os
import sys
import threading


_REAL_STDERR = sys.stderr


# ##########################################################
# helper functions

def _apply_logging_environment():
    """
    Apply the first recognised logging environment variables.
    """

    global _flush_threshold

    enabled = _bool_from_named_env(_ENABLE_LOGGING_NAMES)

    if enabled is not None:

        enable_logging(enabled)

    threshold = _threshold_from_env(_LOGGING_THRESHOLD_NAMES)

    if threshold is not None:

        set_log_filter(threshold)

    _flush_threshold = _threshold_from_env(_FLUSH_THRESHOLD_NAMES)


def _emit_to_stdlib(severity, message):
    """
    Emits conditionally to the standard logging library.
    """

    level = _severity_to_stdlib_level(severity)

    if callable(message):

        if not _stdlib_logger.isEnabledFor(level):

            return

        message = message()

    _stdlib_logger.log(level, str(message))


def _get_stderr_dynamic():

    return sys.stderr


def _get_stderr_static():

    return _REAL_STDERR


def _get_log_file_or_default(file):

    if file:

        return file

    return _get_stderr_dynamic()


def _route_log(file, severity, message):
    """
    Sends a record to the standard logger if one is set and no `file` is
    given; otherwise to the file, or the standard error stream by default.
    """

    if not file and _stdlib_logger is not None:

        _emit_to_stdlib(severity, message)

        return

    _do_log(_get_log_file_or_default(file), severity, message)


def _severity_is_logged(severity):

    if not _logging_is_enabled:

        return False

    if _log_filter:

        if isinstance(_log_filter, (dict,)):
            r = _log_filter.get(severity, _others_action)

            if not r:

                return False
        elif callable(_log_filter):

            if not _log_filter(severity):

                return False
        else:

            if int(severity) > int(_log_filter):

                return False

    return True


def _severity_to_stdlib_level(severity):
    """
    Maps a Diagnosticism severity to a standard `logging` level.
    """

    if severity <= _severity.CRITICAL:

        return stdlib_logging.CRITICAL

    if severity <= _severity.FAILURE:

        return stdlib_logging.ERROR

    if severity <= _severity.WARNING:

        return stdlib_logging.WARNING

    if severity <= _severity.INFORMATIONAL:

        return stdlib_logging.INFO

    return stdlib_logging.DEBUG


def _threshold_from_env(names):

    for name in names:

        if name not in os.environ:

            continue

        try:

            return _severity.parse_verbosity(os.environ[name])
        except ValueError:

            continue

    return None


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


# ##########################################################
# runtime shared state

_logging_is_enabled =   None
_log_filter         =   None
_others_action      =   None
_flush_threshold    =   None
_stdlib_logger      =   None

_ENABLE_LOGGING_NAMES = (
    'DIAGNOSTICISM_ENABLE_LOGGING',
    'SIS_ENABLE_LOGGING',
    'ENABLE_LOGGING',
)

_LOGGING_THRESHOLD_NAMES = (
    'DIAGNOSTICISM_LOGGING_THRESHOLD',
    'SIS_LOGGING_THRESHOLD',
    'LOGGING_THRESHOLD',
    'SIS_SEVERITY_CEILING',
)

_FLUSH_THRESHOLD_NAMES = (
    'DIAGNOSTICISM_FLUSH_THRESHOLD',
    'SIS_FLUSH_THRESHOLD',
    'FLUSH_THRESHOLD',
    'SIS_FLUSH_CEILING',
)


# ##########################################################
# API functions

def enable_logging(*args):
    """
    Enables/disables logging.

    Parameters
    ----------
    *args
        1 or 2 arguments: if 1, then is a `bool` determining whether
        enabled; if 2, then first is name(s) of environment variable(s) to
        be parsed and second is a `bool` specifying the default if not
        found in the environment

    Returns
    -------
    bool
        The previous enable/disable setting

    Raises
    ------
    ValueError
        If the string form of `v` does not contain a recognisable severity
        level
    """

    is_enabled = _bool_from_env(args, 'enable_logging')

    assert(is_enabled == True or is_enabled == False or is_enabled is None)

    global _logging_is_enabled

    with _output_lock:

        _logging_is_enabled, is_enabled = is_enabled, _logging_is_enabled

        return is_enabled


def is_logging_enabled():
    """
    Indicate whether logging is enabled
    """

    with _output_lock:

        return _logging_is_enabled


def is_severity_logged(severity):
    """
    Indicates whether the given severity is logged

    Returns
    -------
    bool
        `True` if the severity is to be logged; `False` otherwise
    """

    with _output_lock:

        return _severity_is_logged(severity)


def set_log_filter(
    log_filter,
    others_action=None,
):
    """
    Sets a logging filter, which may specify a threshold severity, a
    mapping of levels to actions, or a callable

    Parameters
    ----------
    log_filter : int, dict, callable
        If a dictionary, it is interpreted as a mapping from
        severity-level to `True`/`False` that controls each level's output.
        If a callable, it is called with the severity and its result
        decides whether that severity is logged. Otherwise, treated as a
        severity-level threshold (and must be convertible to `int`)

    others_action : obj, optional
        An object to be passed to be used in the case that the log_filter is
        a dictionary and the severity is not recognised

    Returns
    -------
    tuple
        Tuple of the previous (log_filter, others_action) value(s)
    """

    assert log_filter is None or isinstance(log_filter, (dict, )) or callable(log_filter) or isinstance(int(log_filter), int)

    global _log_filter, _others_action

    with _output_lock:

        _log_filter, log_filter, _others_action, others_action = log_filter, _log_filter, others_action, _others_action

        return (log_filter, others_action)


def set_log_logger(logger):
    """
    Sets the standard `logging` logger that receives records that are not
    given an explicit `file`, in place of the standard error stream.

    Parameters
    ----------
    logger : logging.Logger or None
        The logger to use, or `None` to restore the standard error stream.
        Records given an explicit `file` are always written to that file.

    Returns
    -------
    logging.Logger or None
        The previous logger
    """

    global _stdlib_logger

    with _output_lock:

        _stdlib_logger, logger = logger, _stdlib_logger

        return logger


def _do_log(
    file,
    severity,
    message,
):
    """
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

    if callable(message):
        message = message()

    # TODO: perf test this
    full = prefix + ": " + str(message)

    show_program_name = False
    trailing_prompt = False

    file = _get_cr_file_or_default(file)

    _do_report(
        file,
        full,
        show_program_name,
        trailing_prompt,
    )

    if _flush_threshold is not None and int(severity) <= int(_flush_threshold):

        flush = getattr(file, 'flush', None)

        if flush:

            flush()


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
        A message string to be emitted, or a callable object that will yield
        an emittable string when called

    Returns
    -------
    None
    """

    with _output_lock:

        if not _severity_is_logged(severity):

            return

        return _route_log(file, severity, message)


# ##########################################################
# initialisation

_apply_logging_environment()


# ############################## end of file ############################# #

