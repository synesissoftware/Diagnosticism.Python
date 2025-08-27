
from .internal import (
    _is_python_2_7_or_later,
    _is_python_3_0_or_later,
)


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
"""Severity level suitable for use when logging that a design violation has occurred."""
ALERT           =   2
"""Severity level suitable for use when logging that a fatal program failure has occurred."""
CRITICAL        =   3
"""Severity level suitable for use when logging that a critical failure has occurred."""
FAILURE         =   4
"""Severity level suitable for use when logging that a failure has occurred."""
WARNING         =   5
"""Severity level suitable for use when issuing a warning."""
NOTICE          =   6
"""Severity level suitable for use when logging an important normative condition."""
INFORMATIONAL   =   7
"""Severity level suitable for use when logging a normative condition."""
DEBUG0          =   8
"""The highest debug severity level."""
DEBUG1          =   9
"""The second highest debug severity level."""
DEBUG2          =   10
"""The third highest debug severity level."""
DEBUG3          =   11
"""The fourth highest debug severity level."""
DEBUG4          =   12
"""The fifth highest debug severity level."""
DEBUG5          =   13
"""The sixth highest debug severity level."""
TRACE           =   14
"""Severity level suitable at which trace statements are issued."""
BENCHMARK       =   15
"""Severity level suitable at which benchmark statements are issued."""

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
    'VIOLATION'                 :   VIOLATION,
    'ALERT'                     :   ALERT,
    'CRITICAL'                  :   CRITICAL,
    'FAILURE'                   :   FAILURE,
    'WARNING'                   :   WARNING,
    'NOTICE'                    :   NOTICE,
    'INFORMATIONAL'             :   INFORMATIONAL,
    'DEBUG0'                    :   DEBUG0,
    'DEBUG1'                    :   DEBUG1,
    'DEBUG2'                    :   DEBUG2,
    'DEBUG3'                    :   DEBUG3,
    'DEBUG4'                    :   DEBUG4,
    'DEBUG5'                    :   DEBUG5,
    'TRACE'                     :   TRACE,
    'BENCHMARK'                 :   BENCHMARK,

    # stock shorthands
    'FAIL'                      :   FAILURE,
    'WARN'                      :   WARNING,
    'INFO'                      :   INFORMATIONAL,

    # de-facto public synonyms
    'EMERGENCY'                 :   VIOLATION,
    'ERROR'                     :   FAILURE,
    'DEBUG'                     :   DEBUG5,

    # de-facto public shorthands
    'ALRT'                      :   ALERT,
    'CRIT'                      :   CRITICAL,
    'ERR'                       :   FAILURE,
    'TRC'                       :   TRACE,
    'BENCH'                     :   BENCHMARK,
}

if _is_python_3_0_or_later():

    _INTEGER_TYPES = (int, )
else:

    _INTEGER_TYPES = (int, long, ) # noqa: F821


def _parse_verbosity(
    v,
    strict_case_comparison,
):
    """
    Parses the verbosity from `v`.

    Parameters
    ----------
    v : str | int | *
        The variable from which to parse the verbosity. If an integer, is taken as is; if not a string then converted to a string, and in either case is then subject to parsing
    strict_case_comparison : bool
        Specifies whether any string comparison should be strict or permissive

    Returns
    -------
    int
        The severity level

    Raises
    ------
    ValueError
        If the string form of `v` does not contain a recognisable severity level
    """

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


if _is_python_2_7_or_later():

    def parse_verbosity(
        v,
        **kwargs,
    ):
        """
        Attempts to parse the verbosity from `v`.

        Parameters
        ----------
        v : str | int | *
            The variable from which to parse the verbosity. If an integer, is taken as is; if not a string is converted to a string, and in either case is then subject to parsing
        kwargs : dict
            Keyword arguments. Currently only `strict_case_comparison` is recognised, which defaults to `False` if not specified by the caller

        Returns
        -------
        int
            The severity level

        Raises
        ------
        ValueError
            If the string form of `v` does not contain a recognisable severity level
        """

        strict_case_comparison = kwargs.get('strict_case_comparison', False)


        return _parse_verbosity(
            v,
            strict_case_comparison=strict_case_comparison,
        )
else:

    def parse_verbosity(
        v,
    ):
        """
        Attempts to parse the verbosity from `v`.

        Parameters
        ----------
        v : str | int | *
            The variable from which to parse the verbosity. If an integer, is taken as is; if not a string is converted to a string, and in either case is then subject to parsing

        Returns
        -------
        int
            The severity level

        Raises
        ------
        ValueError
            If the string form of `v` does not contain a recognisable severity level
        """

        return _parse_verbosity(
            v,
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


# ############################## end of file ############################# #

