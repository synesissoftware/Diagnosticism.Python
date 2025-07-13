
import sys

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
    'INFO',

    'parse_verbosity',
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

DEBUG           =   DEBUG5
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

_STRINGS_RECOGNISABLE_AS_SEVERITY_LEVELS = {

    # actual values
    "VIOLATION"                 :   VIOLATION,
    "ALERT"                     :   ALERT,
    "CRITICAL"                  :   CRITICAL,
    "FAILURE"                   :   FAILURE,
    "WARNING"                   :   WARNING,
    "NOTICE"                    :   NOTICE,
    "INFORMATIONAL"             :   INFORMATIONAL,
    "DEBUG0"                    :   DEBUG0,
    "DEBUG1"                    :   DEBUG1,
    "DEBUG2"                    :   DEBUG2,
    "DEBUG3"                    :   DEBUG3,
    "DEBUG4"                    :   DEBUG4,
    "DEBUG5"                    :   DEBUG5,
    "TRACE"                     :   TRACE,
    "BENCHMARK"                 :   BENCHMARK,

    # stock shorthands
    "FAIL"                      :   FAILURE,
    "WARN"                      :   WARNING,
    "INFO"                      :   INFORMATIONAL,

    # de-facto public synonyms
    "EMERGENCY"                 :   VIOLATION,
    "ERROR"                     :   FAILURE,
    "DEBUG"                     :   DEBUG5,

    # de-facto public shorthands
    "ALRT"                      :   ALERT,
    "CRIT"                      :   CRITICAL,
    "ERR"                       :   FAILURE,
    "TRC"                       :   TRACE,
    "BENCH"                     :   BENCHMARK,
}

if sys.version_info[:2] >= (3, 0):

    _INTEGER_TYPES = (int, )
else:

    _INTEGER_TYPES = (int, long, )


def _parse_verbosity(
    v,
    strict_case_comparison,
):

    if isinstance(v, _INTEGER_TYPES):

        return v

    if isinstance(v, str):

        s = v.strip()
    else:

        s = str(v)

    severity = _STRINGS_RECOGNISABLE_AS_SEVERITY_LEVELS.get(s, None)
    if severity == None and not strict_case_comparison:

        s_upper = s.upper()

        severity = _STRINGS_RECOGNISABLE_AS_SEVERITY_LEVELS.get(s_upper, None)

    if severity != None:

        return severity

    try:

        return int(s)
    except ValueError as x:

        raise ValueError("could not recognise value '%s' as a severity" % (v))


if sys.version_info[:2] >= (2, 7):

    def parse_verbosity(
        s,
        **kwargs,
    ):
        """
        Attempts to recognise

        Parameters
        ----------
        s : str, int

        Returns
        -------

        TBC
        """

        strict_case_comparison = kwargs.get('strict_case_comparison', False)


        return _parse_verbosity(
            s,
            strict_case_comparison=strict_case_comparison,
        )
else:

    def parse_verbosity(
        s,
    ):
        """
        TBC
        """

        return _parse_verbosity(
            s,
            False, # strict_case_comparison
        )


def severity_to_string(severity):
    """
    Converts a severity to its string form

    Parameters
    ----------
    severity : int
        The severity associated with the message

    Returns
    -------
    str
        The string corresponding to the severity
    """

    s = _STOCK_SEVERITY_LEVELS.get(severity, None)

    if s is None:

        if isinstance(severity, _INTEGER_TYPES):

            s = str(severity)
        else:

            s = "%s (%s)" % (str(severity), type(severity))

        return "<Severity: %s>" % s
    else:

        return s

