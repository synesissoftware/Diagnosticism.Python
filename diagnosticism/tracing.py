
from .logging import do_log
from . import severity
from .internal import _basename

import inspect


_tracingEnabled =   False


def _derive_param(pname, params):

    val = params[pname]
    typ = val.__class__.__name__

    return (pname, typ, val)


def _flf(
        depth=1,
        **kwargs,
    ):

    assert 1 == depth

    fr = inspect.currentframe()

    try:

        fr = fr.f_back
        fr = fr.f_back

        code = fr.f_code

        file_name   =   code.co_filename
        line_number =   fr.f_lineno
        if '<module>' == code.co_name:

            function_name   =   "<module>"
        else:

            function_name   =   code.co_name

        if kwargs.get('basename', False):

            file_name = _basename(file_name)

        return [ file_name, line_number, function_name ]
    finally:

        del fr


def _log_s(severity, message):

    do_log(severity, message)


def enable_tracing(is_enabled):
    """
    Enables/disables tracing

    Parameters
    ----------
    is_enabled : bool
        Determines whether tracing will be enabled/disabled

    Returns
    -------
    bool
        The previous enable/disable setting
    """

    assert(is_enabled == True or is_enabled == False)

    global _tracingEnabled

    _tracingEnabled = is_enabled


def file(
        **kwargs,
    ):
    """
    Obtains the file of the caller.

    Returns
    -------
    str
    """

    return _flf(depth=1, **kwargs)[0]


def func(
        **kwargs,
    ):
    """
    Obtains the function of the caller.

    Returns
    -------
    str
    """

    return _flf(depth=1)[2]


def line(
        **kwargs,
    ):
    """
    Obtains the line of the caller.

    Returns
    -------
    int
    """

    return _flf(depth=1)[1]


def fileline(
        **kwargs,
    ):
    """
    Obtains a string representing the file and line of the caller.

    Returns
    -------
    str
        String of the form "file:line".
    """

    sep = kwargs.get('sep', ':')

    flf = _flf(depth=1, **kwargs)

    return flf[0] + sep + str(flf[1])


def filelinefunc(
        **kwargs,
    ):
    """
    Obtains a string representing the file, line, and function of the
    caller.

    Returns
    -------
    str
        String of the form "file:line:func".
    """

    sep = kwargs.get('sep', ':')

    flf = _flf(depth=1, **kwargs)

    return flf[0] + sep + str(flf[1]) + sep + flf[2]


def is_tracing_enabled():
    """
    Indicate whether tracing is enabled

    Returns
    -------
    bool
    """

    return _tracingEnabled


def trace():
    """
    Traces function signature, including parameters, of the calling function

    Returns
    -------
    None
    """

    if _tracingEnabled:

        fr = inspect.currentframe()

        try:

            fr = fr.f_back

            code = fr.f_code

            if '<module>' == code.co_name:

                _log_s(severity.TRACE, "%s:%d" % (code.co_filename, code.co_firstlineno))
            else:

                fname = code.co_name
                vnames = code.co_varnames
                params = fr.f_locals

                pnames = [vname for vname in vnames if vname in params]


                # Algorithm informed by http://blog.mclemon.io/python-efficient-string-concatenation-in-python-2016-edition

                if 0 != len(pnames):

                    pname0 = pnames[0]

                    if 'self' == pname0:

                        val0 = params[pname0]
                        typ0 = val0.__class__.__name__

                        plist = ", ".join(["%s(%s)=%s" % _derive_param(pname, params) for pname in pnames[1:]])

                        _log_s(severity.TRACE, "%s.%s(%s)" % (typ0, fname, plist))

                        return

                plist = ", ".join(["%s(%s)=%s" % _derive_param(pname, params) for pname in pnames])

                _log_s(severity.TRACE, "%s(%s)" % (fname, plist))
        finally:

            del fr

