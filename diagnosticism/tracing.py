
from .logging import (
    _do_log,
    _get_log_file_or_default,
)
from . import severity

from .internal import (
    _basename,
    _bool_from_env,
    _is_python_3_9_or_later,
)

import inspect
import sys


_tracingEnabled =   False


def _derive_param(
    param_name, # : str
    params, # : list[str]
):
    """
    xxx.

    Returns
    -------
    tuple
        Tuple of the previous (param_name, param_type, param_value) value(s)
    """

    param_value =   params[param_name]
    param_type  =   param_value.__class__.__name__

    return (param_name, param_type, param_value)


def _dbg(
    file,
    fr,
    show_fileline,
    *args,
    **kwargs,
):

    try:

        fr = fr.f_back

        code = fr.f_code

        file_name   =   code.co_filename
        line_number =   fr.f_lineno

        vnames = code.co_varnames
        params = fr.f_locals

        kwnames = list(kwargs)

        if 0 != len(args):

            s0 = ', '.join(["(%s)=%s" % (type(arg).__name__, arg) for arg in args])
        else:

            s0 = ''

        if 0 != len(kwargs):

            s1 = ', '.join(["%s(%s)=%s" % (name, type(arg).__name__, arg) for name, arg in kwargs.items()])
        else:

            s1 = ''

        if s0 and s1:

            s = ", ".join([s0, s1])
        elif s0:

            s = s0
        elif s1:

            s = s1
        else:

            s = ''

        if show_fileline:

            _log_s(file, severity.TRACE, "%s:%s: %s" % (_basename(file_name), line_number, s))
        else:

            _log_s(file, severity.TRACE, "%s" % s)
    finally:

        del fr


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


def _log_s(
    file,
    severity,
    message,
):

    file = _get_log_file_or_default(file)

    _do_log(
        file,
        severity,
        message,
    )


def dbgfl(
    *args,
    **kwargs,
):
    """
    Traces arguments and keyword-arguments with file + line.

    Returns
    -------
    None
    """

    if _tracingEnabled:

        fr = inspect.currentframe()

        file = kwargs.get('file', None)

        _dbg(
            file,
            fr,
            True,
            *args,
            **kwargs,
        )


def dbg(
    *args,
    **kwargs,
):
    """
    Traces arguments and keyword-arguments.

    Returns
    -------
    None
    """

    if _tracingEnabled:

        fr = inspect.currentframe()

        file = kwargs.get('file', None)

        _dbg(
            file,
            fr,
            False,
            *args,
            **kwargs,
        )


def enable_tracing(*args):
    """
    Enables/disables tracing.

    Parameters
    ----------
    *args
        1 or 2 arguments: if 1, then is a `bool` determining whether should be enabled; if 2, then first is name(s) of environment variable(s) to be parsed and second is a `bool` specifying the default if not found in the environment

    Returns
    -------
    bool
        The previous enable/disable setting
    """

    is_enabled = _bool_from_env(args, 'enable_tracing')

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


def trace(
    file=None,
):
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

                _log_s(file, severity.TRACE, "%s:%d" % (code.co_filename, code.co_firstlineno))
            else:

                fname   =   code.co_name
                vnames  =   code.co_varnames
                params  =   fr.f_locals

                pnames  =   [vname for vname in vnames if vname in params]

                # Algorithm informed by http://blog.mclemon.io/python-efficient-string-concatenation-in-python-2016-edition

                if 0 != len(pnames):

                    pname0 = pnames[0]

                    if 'self' == pname0:

                        val0    =   params[pname0]
                        typ0    =   val0.__class__.__name__

                        plist   =   ", ".join(["%s(%s)=%s" % _derive_param(pname, params) for pname in pnames[1:]])

                        _log_s(file, severity.TRACE, "%s.%s(%s)" % (typ0, fname, plist))

                        return

                plist = ", ".join(["%s(%s)=%s" % _derive_param(pname, params) for pname in pnames])

                _log_s(file, severity.TRACE, "%s(%s)" % (fname, plist))
        finally:

            del fr


if _is_python_3_9_or_later():

    def tracefunc(
        func,
        file=None,
    ):
        """
        Decorator function that equates to the receiver function calling `trace()`

        Returns
        -------
            A wrapper function that calls the decorated function
        """

        def wrapper(*args, **kwargs):

            if is_tracing_enabled():

                sig =   None

                try:

                    sig         =   inspect.signature(func) # py 3.3

                    params      =   sig.parameters
                    params_l    =   list([(k, v) for (k, v) in params.items()])
                    args_n      =   args

                    # S=self, N=normal, A=*args, K=**kwargs

                    paramA      =   None
                    paramK      =   None

                    partN       =   None
                    partA       =   None
                    partK       =   None

                    typeS       =   None

                    if len(params_l) != 0:

                        if 'self' == params_l[0][0]:

                            typeS   =   args[0].__class__.__name__
                            args_n  =   args[1:]

                    if len(params_l) != 0:

                        if params_l[-1][1].kind == inspect.Parameter.VAR_KEYWORD:

                            paramK  =   params_l.pop()
                            partK   =   f"{paramK[0]}(dict)={kwargs}"

                    if len(params_l) != 0:

                        if params_l[-1][1].kind == inspect.Parameter.VAR_POSITIONAL:

                            paramA  =   params_l.pop()
                            partA   =   f"{paramA[0]}(tuple)={args_n[len(params_l):]}"

                    if len(params_l) != 0:

                        namesN  =   [p[0] for p in params_l]
                        partN   =   ', '.join([f"{k}({v.__class__.__name__})={v}" for (k, v) in dict(zip(namesN, args_n)).items()])


                    fname   =   func.__name__


                    args_list = []

                    if partN and len(partN) != 0:

                        args_list.append(partN)

                    if partA and len(partA) != 0:

                        args_list.append(partA)

                    if partK and len(partK) != 0:

                        args_list.append(partK)

                    plist = ', '.join(args_list)


                    if typeS:

                        _log_s(file, severity.TRACE, "%s.%s(%s)" % (typeS, fname, plist))
                    else:

                        _log_s(file, severity.TRACE, "%s(%s)" % (fname, plist))
                finally:

                    del sig

            return func(*args, **kwargs)

        return wrapper

    def asynctracefunc(
        func,
        file=None,
    ):
        """
        Async decorator function that equates to the receiver function calling `trace()`

        Returns
        -------
            A wrapper function that calls the decorated function
        """

        return tracefunc(func, file)


# ############################## end of file ############################# #

