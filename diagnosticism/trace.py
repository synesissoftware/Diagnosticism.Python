
from .log import do_log
from . import severity

import inspect

_tracingEnabled =   False

def _derive_param(pname, params):

    val = params[pname]
    typ = val.__class__.__name__

    return (pname, typ, val)

def _log_s(severity, message):

    do_log(severity, message)

def enable_tracing(enabled):

    global _tracingEnabled

    _tracingEnabled = enabled

def is_tracing_enabled():

    return _tracingEnabled

def trace():

    if _tracingEnabled:

        fr = inspect.currentframe()

        try:

            fr = fr.f_back

            code = fr.f_code

            fname = code.co_name
            vnames = code.co_varnames
            params = fr.f_locals

            pnames = [n for n in vnames if n in params]

            # Algorithm informed by http://blog.mclemon.io/python-efficient-string-concatenation-in-python-2016-edition

            if 0 != len(params):

                pname0 = pnames[0]

                if 'self' == pname0:

                    val0 = params[pname0]
                    typ0 = val0.__class__.__name__

                    plist = ", ".join(["%s(%s)=%s" % _derive_param(n, params) for n in pnames[1:]])

                    _log_s(severity.TRACE, "%s.%s(%s)" % (typ0, fname, plist))

                    return

            plist = ", ".join(["%s(%s)=%s" % _derive_param(n, params) for n in pnames])

            _log_s(severity.TRACE, "%s(%s)" % (fname, plist))
        finally:

            del fr

