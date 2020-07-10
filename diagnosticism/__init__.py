
__author__      =   'Matt Wilson'
__copyright__   =   'Copyright 2019-2020, Synesis Information Systems, Copyright 2019, Synesis Software'
__credits__     =   [
        'Garth Lancaster',
        'Matt Wilson',
 ]
__email__       =   'matthew@synesis.com.au'
__license__     =   'BSD-3-Clause'
__maintainer__  =   'Matt Wilson'
__status__      =   'Beta'
__version__     =   '0.4.0'

from .conrep import abort, report
from .log import enable_logging, is_logging_enabled, log
from .program_name import *
from .severity import *
from .trace import enable_tracing, is_tracing_enabled, trace

