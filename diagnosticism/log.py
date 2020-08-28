
from datetime import datetime as dt
import os
import sys
import threading

from .conrep import report, _isatty
from .program_name import get_program_name
from . import severity as _severity

class _clrs:

    RED         =   '\x1B[31m'
    GREEN       =   '\x1B[32m'
    YELLOW      =   '\x1B[33m'
    BLUE        =   '\x1B[34m'
    MAGENTA     =   '\x1B[35m'
    DARKGREY    =   '\x1B[90m'
    NONE        =   '\x1B[0m'

    D   =   {

        _severity.VIOLATION       :   RED,
        _severity.ALERT           :   RED,
        _severity.CRITICAL        :   RED,
        _severity.FAILURE         :   RED,
        _severity.WARNING         :   YELLOW,
        _severity.NOTICE          :   MAGENTA,
        _severity.INFORMATIONAL   :   MAGENTA,
        _severity.DEBUG0          :   BLUE,
        _severity.DEBUG1          :   BLUE,
        _severity.DEBUG2          :   BLUE,
        _severity.DEBUG3          :   BLUE,
        _severity.DEBUG4          :   BLUE,
        _severity.DEBUG5          :   BLUE,
        _severity.TRACE           :   DARKGREY,
        _severity.BENCHMARK       :   DARKGREY,
    }


_logging_is_enabled =   None
_log_filter         =   None
_others_action      =   None

def enable_logging(is_enabled):
    """Enables/disables logging

    Parameters
    ----------
    is_enabled : boolean
        Determines whether logging will be enabled/disabled

    Returns
    -------
    The previous enable/disable setting
"""

    assert(is_enabled == True or is_enabled == False or is_enabled is None)

    global _logging_is_enabled

    _logging_is_enabled, is_enabled = is_enabled, _logging_is_enabled

    return is_enabled

def is_logging_enabled():
    """Indicate whether logging is enabled"""

    return _logging_is_enabled

def set_log_filter(log_filter, others_action=None):
    """Sets a logging filter, which may either specify a threshold severity or a mapping of levels to actions

    Parameters
    ----------
    log_filter : severity-level, dict
        If a dictionary, it is interpreted as a mapping from severity-level to True/False that controls each level's output; otherwise, treated as a severity-level threshold (and must be convertible to int)

    Returns
    -------
    Tuple of the previous (log_filter, others_action) value(s)
"""

    assert log_filter is None or isinstance(log_filter, (dict, )) or isinstance(int(log_filter), int)

    global _log_filter, _others_action

    _log_filter, log_filter, _others_action, others_action = log_filter, _log_filter, others_action, _others_action

    return (log_filter, others_action)


def do_log(severity, message):

    now = dt.now()

    ss = _severity.severity_to_string(severity)

    if _isatty():

        r = _clrs.D.get(severity, None)

        if r:

            ss = r + ss + _clrs.NONE

    prefix = "[%s, %s, %s, %s]" % (get_program_name(), threading.current_thread().ident, str(now), ss)

    if hasattr(message, '__call__'):

        message = message()

    full = prefix + ': ' + message

    report(full, show_program_name=False)

def log(severity, message):
    """Conditionally issue the given log message based on the given severity

    Parameters
    ----------
    severity : int
        The severity associated with the message

    message : str, callable
        A message string to be emitted, or a callable object that will yield an emittable string when called

    Return
    ------
    None
"""

    if _logging_is_enabled is None:

        # use filter

        if _log_filter:

            if isinstance(_log_filter, (dict, )):

                r = _log_filter.get(severity, _others_action)

                if not r:

                    return
            else:

                if int(severity) > int(_log_filter):

                    return
        else:

            return
    else:

        if not _logging_is_enabled:

            return


    return do_log(severity, message)


