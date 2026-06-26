
__author__      =   'Matt Wilson'
__copyright__   =   'Copyright 2019-2025, Synesis Information Systems, Copyright 2019, Synesis Software'
__credits__     =   [
    'Garth Lancaster',
    'Matt Wilson',
]
__email__       =   'matthew@synesis.com.au'
__license__     =   'BSD-3-Clause'
__maintainer__  =   'Matt Wilson'
__status__      =   'Beta'
__version__     =   '0.15.3'

import sys

from .contingent_reporting import (
    abort,
    report,
    set_default_trailing_prompt,
)
from .doomgram import (
    DOOMGram,
    DOOMScope,
)
from .logging import (
    enable_logging,
    is_logging_enabled,
    is_severity_logged,
    log,
    set_log_filter,
)
from .program_name import (
    get_program_name,
    set_program_name,
)
from .severity import (
    ALERT,
    BENCHMARK,
    CRITICAL,
    DEBUG0,
    DEBUG1,
    DEBUG2,
    DEBUG3,
    DEBUG4,
    DEBUG5,
    FAIL,
    FAILURE,
    INFO,
    INFORMATIONAL,
    NOTICE,
    TRACE,
    UNSPECIFIED,
    VIOLATION,
    WARN,
    WARNING,
    parse_verbosity,
    severity_to_string,
)
from .tracing import (
    dbg,
    dbgfl,
    enable_tracing,
    file,
    fileline,
    filelinefunc,
    func,
    is_tracing_enabled,
    line,
    trace,
)
if sys.version_info[:2] >= (3, 9):
    from .tracing import (
        asynctracefunc,
        tracefunc,
    )

from .warning import warn


__all__ = [
    '__version__',

    'ALERT',
    'BENCHMARK',
    'CRITICAL',
    'DEBUG0',
    'DEBUG1',
    'DEBUG2',
    'DEBUG3',
    'DEBUG4',
    'DEBUG5',
    'DOOMGram',
    'DOOMScope',
    'FAIL',
    'FAILURE',
    'INFO',
    'INFORMATIONAL',
    'NOTICE',
    'TRACE',
    'UNSPECIFIED',
    'VIOLATION',
    'WARN',
    'WARNING',
    'abort',
    'dbg',
    'dbgfl',
    'enable_logging',
    'enable_tracing',
    'file',
    'fileline',
    'filelinefunc',
    'func',
    'get_program_name',
    'is_logging_enabled',
    'is_severity_logged',
    'is_tracing_enabled',
    'line',
    'log',
    'parse_verbosity',
    'report',
    'set_default_trailing_prompt',
    'set_log_filter',
    'set_program_name',
    'severity_to_string',
    'trace',
    'warn',
]

if sys.version_info[:2] >= (3, 9):
    __all__.extend([
        'asynctracefunc',
        'tracefunc',
    ])


# ############################## end of file ############################# #

