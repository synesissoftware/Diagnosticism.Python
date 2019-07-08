
__all__ = [

    'UNSPECIFIED',
    'VIOLATION',
    'ALERT',
    'CRITICAL',
    'FAILURE',
    'WARNING',
    'NOTICE',
    'INFORMATIONAL',
    'DEBUG0',
    'DEBUG1',
    'DEBUG2',
    'DEBUG3',
    'DEBUG4',
    'DEBUG5',
    'TRACE',
    'BENCHMARK',

    'FAIL',
    'WARN',

    'severity_to_string',
]

UNSPECIFIED     =   0
VIOLATION       =   1
ALERT           =   2
CRITICAL        =   3
FAILURE         =   4
WARNING         =   5
NOTICE          =   6
INFORMATIONAL   =   7
DEBUG0          =   8
DEBUG1          =   9
DEBUG2          =   10
DEBUG3          =   11
DEBUG4          =   12
DEBUG5          =   13
TRACE           =   14
BENCHMARK       =   15

FAIL            =   FAILURE
WARN            =   WARNING
INFO            =   INFORMATIONAL

_STOCK_SEVERITY_LEVELS = {

    VIOLATION       :   'VIOLATION',
    ALERT           :   'ALERT',
    CRITICAL        :   'CRITICAL',
    FAILURE         :   'FAILURE',
    WARNING         :   'WARNING',
    NOTICE          :   'NOTICE',
    INFORMATIONAL   :   'INFORMATIONAL',
    DEBUG0          :   'DEBUG0',
    DEBUG1          :   'DEBUG1',
    DEBUG2          :   'DEBUG2',
    DEBUG3          :   'DEBUG3',
    DEBUG4          :   'DEBUG4',
    DEBUG5          :   'DEBUG5',
    TRACE           :   'TRACE',
    BENCHMARK       :   'BENCHMARK',
}



def severity_to_string(severity):

    s = _STOCK_SEVERITY_LEVELS.get(severity, None)

    if s is None:

        if isinstance(severity, (int, long, )):

            s = str(severity)
        else:

            s = "%s (%s)" % (str(severity), type(severity))

        return "<Severity: %s>" % s
    else:

        return s



