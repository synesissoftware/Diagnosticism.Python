
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
__version__     =   '0.14.0'

from .contingent_reporting import (
    abort,
    report,
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
from .program_name import *
from .severity import *
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
    tracefunc,
)
from .warning import warn


# ############################## end of file ############################# #

