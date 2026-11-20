
from .contingent_reporting import _output_lock
from .logging import (
    _do_log,
    _get_log_file_or_default,
)
from . import severity

from .internal import (
    _basename,
    _bool_from_env,
    _is_python_2_7_or_later,
)

import functools
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
    **kwargs
):

    try:

        fr = fr.f_back

        code = fr.f_code

        file_name   =   code.co_filename
        line_number =   fr.f_lineno


        kwargs.pop('file', None)

        if 0 != len(args):
            s0 = ", ".join(["(%s)=%s" % (type(arg).__name__, arg) for arg in args])
        else:
            s0 = ""

        if 0 != len(kwargs):
            s1 = ", ".join(["%s(%s)=%s" % (name, type(arg).__name__, arg) for name, arg in kwargs.items()])
        else:
            s1 = ""

        if s0 and s1:

            s = ", ".join([s0, s1])
        elif s0:

            s = s0
        elif s1:

            s = s1
        else:

            s = ""

        if show_fileline:

            _log_s(file, severity.TRACE, "%s:%s: %s" % (_basename(file_name), line_number, s))
        else:

            _log_s(file, severity.TRACE, "%s" % s)
    finally:

        del fr


def _flf(
    depth=1,
    **kwargs
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
            function_name   =   '<module>'
        else:

            function_name   =   code.co_name

        if kwargs.get('basename', False):

            file_name = _basename(file_name)

        return [file_name, line_number, function_name]
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
    **kwargs
):
    """
    Traces arguments and keyword-arguments with file + line.

    Returns
    -------
    None
    """

    if _tracingEnabled:

        fr = inspect.currentframe()

        file = kwargs.pop('file', None)

        _dbg(
            file,
            fr,
            True,
            *args,
            **kwargs
        )


def dbg(
    *args,
    **kwargs
):
    """
    Traces arguments and keyword-arguments.

    Returns
    -------
    None
    """

    if _tracingEnabled:

        fr = inspect.currentframe()

        file = kwargs.pop('file', None)

        _dbg(
            file,
            fr,
            False,
            *args,
            **kwargs
        )


def enable_tracing(*args):
    """
    Enables/disables tracing.

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
    """

    is_enabled = _bool_from_env(args, 'enable_tracing')

    assert(is_enabled == True or is_enabled == False)

    global _tracingEnabled

    with _output_lock:

        _tracingEnabled, is_enabled = is_enabled, _tracingEnabled

        return is_enabled


def file(
    **kwargs
):
    """
    Obtains the file of the caller.

    Returns
    -------
    str
    """

    return _flf(depth=1, **kwargs)[0]


def func(
    **kwargs
):
    """
    Obtains the function of the caller.

    Returns
    -------
    str
    """

    return _flf(depth=1, **kwargs)[2]


function = func


def line(
    **kwargs
):
    """
    Obtains the line of the caller.

    Returns
    -------
    int
    """

    return _flf(depth=1, **kwargs)[1]


def fileline(
    **kwargs
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
    **kwargs
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

    with _output_lock:

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

                _log_s(file, severity.TRACE, "%s:%d" % (code.co_filename, fr.f_lineno))
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


def _log_traced_py2(
    file,
    func,
    is_instance_method,
    args,
    kwargs,
):

    spec = inspect.getargspec(func)
    names = list(spec.args)
    args_n = args
    type_name = None

    if is_instance_method and len(names) != 0 and 'self' == names[0]:

        type_name = args[0].__class__.__name__
        names = names[1:]
        args_n = args[1:]

    parts = []

    if len(names) != 0:

        pairs = ["%s(%s)=%s" % (name, value.__class__.__name__, value) for name, value in zip(names, args_n)]

        parts.append(', '.join(pairs))

    if spec.varargs:

        parts.append("%s(tuple)=%s" % (spec.varargs, args_n[len(names):]))

    if spec.keywords:

        parts.append("%s(dict)=%s" % (spec.keywords, kwargs))

    plist = ', '.join(parts)

    if type_name:

        _log_s(file, severity.TRACE, "%s.%s(%s)" % (type_name, func.__name__, plist))
    else:

        _log_s(file, severity.TRACE, "%s(%s)" % (func.__name__, plist))


if _is_python_2_7_or_later():

    def _emit_trace(
        file,
        func,
        is_instance_method,
        args,
        kwargs,
    ):

        if not is_tracing_enabled():

            return

        sig = None

        try:

            if not hasattr(inspect, 'signature'):

                _log_traced_py2(file, func, is_instance_method, args, kwargs)

                return

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

            if is_instance_method and len(params_l) != 0:

                if 'self' == params_l[0][0]:

                    typeS   =   args[0].__class__.__name__
                    args_n  =   args[1:]

            if len(params_l) != 0:

                if params_l[-1][1].kind == inspect.Parameter.VAR_KEYWORD:

                    paramK  =   params_l.pop()
                    partK   =   "%s(dict)=%s" % (paramK[0], kwargs)

            if len(params_l) != 0:

                if params_l[-1][1].kind == inspect.Parameter.VAR_POSITIONAL:

                    paramA  =   params_l.pop()
                    partA   =   "%s(tuple)=%s" % (paramA[0], args_n[len(params_l):])

            if len(params_l) != 0:

                namesN  =   [p[0] for p in params_l]
                partN   =   ', '.join(["%s(%s)=%s" % (k, v.__class__.__name__, v) for (k, v) in dict(zip(namesN, args_n)).items()])


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


    def _async_wrapper(
        func,
        file,
        is_instance_method,
    ):

        namespace = {
            '_emit_trace': _emit_trace,
            'file': file,
            'func': func,
            'functools': functools,
            'is_instance_method': is_instance_method,
        }

        exec(
            "@functools.wraps(func)\n"
            "async def wrapper(*args, **kwargs):\n"
            "    _emit_trace(file, func, is_instance_method, args, kwargs)\n"
            "    return await func(*args, **kwargs)\n",
            namespace,
        )

        return namespace['wrapper']


    def _apply_tracefunc(
        func,
        file,
    ):

        kind = None
        is_instance_method = True

        if isinstance(func, staticmethod):

            kind = staticmethod
            func = func.__func__
            is_instance_method = False
        elif isinstance(func, classmethod):

            kind = classmethod
            func = func.__func__
            is_instance_method = False

        is_coroutine = sys.version_info[0] >= 3 and inspect.iscoroutinefunction(func)

        if is_coroutine:

            wrapper = _async_wrapper(func, file, is_instance_method)
        else:

            @functools.wraps(func)
            def wrapper(*args, **kwargs):

                _emit_trace(file, func, is_instance_method, args, kwargs)

                return func(*args, **kwargs)

        if kind is None:

            return wrapper

        return kind(wrapper)


    def tracefunc(
        func=None,
        file=None,
    ):
        """
        Decorator function that equates to the receiver function calling
        `trace()`.

        Parameters
        ----------
        func : callable, optional
            The function to decorate. Omit it to pass `file`.

        file : file-object, optional
            The log stream. `None` selects the default stream

        Returns
        -------
        callable
            The wrapped function, or a decorator when `func` is omitted
        """

        if func is None:

            def decorator(fn):

                return _apply_tracefunc(fn, file)

            return decorator

        return _apply_tracefunc(func, file)


    def asynctracefunc(
        func=None,
        file=None,
    ):
        """
        Async decorator function that equates to the receiver function
        calling `trace()`.

        Returns
        -------
        callable
            A wrapper function that calls the decorated function
        """

        return tracefunc(func, file)


# ############################## end of file ############################# #

