
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


_logging_is_enabled = False

def enable_logging(is_enabled):

    global _logging_is_enabled

    _logging_is_enabled = is_enabled

def is_logging_enabled():

    return _logging_is_enabled

def do_log(severity, message):

    now = dt.now()

    ss = _severity.severity_to_string(severity)

    if _isatty():

        r = _clrs.D.get(severity, None)

        if r:

            ss = r + ss + _clrs.NONE

    prefix = "[%s, %s, %s, %s]" % (get_program_name(), threading.current_thread().ident, str(now), ss)

    full = prefix + ': ' + message

    report(full, show_program_name=False)

def log(severity, message):

    if not _logging_is_enabled:

        return

    return do_log(severity, message)

