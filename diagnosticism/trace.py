
import inspect
import sys

_tracingEnabled =   False

def _log_s(severity, message):

    sys.stderr.write(message + "\n")

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
            pnames = code.co_varnames
            params = fr.f_locals

            # Algorithm informed by http://blog.mclemon.io/python-efficient-string-concatenation-in-python-2016-edition

            plist = ", ".join(["%s(%s)=%s" % (n, type(params[n]).__name__, params[n]) for n in pnames])

            _log_s(None, "%s(%s)" % (fname, plist))
        finally:

            del fr

