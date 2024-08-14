
from .contingent_reporting import _add_eol_and_emit_to_cr_stm
from .logging import do_log, is_logging_enabled
from . import severity


def warn(message, **kwargs):
    """Analogue of Ruby's Kernel#warn()

    Parameters
    ----------
    message : str, None
        The message to be emitted to the standard error stream (along with a new-line sequence). If None, nothing is emitted
    """

    if message:

        if is_logging_enabled():

            do_log()

        _add_eol_and_emit_to_cr_stm(message)

