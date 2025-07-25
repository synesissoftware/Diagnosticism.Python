
from .contingent_reporting import (
    _add_eol_and_emit_to_cr_stm,
    _get_cr_file_or_default,
)
from .logging import (
    _do_log,
    _get_log_file_or_default,
    is_logging_enabled,
)
from . import severity

import sys


def _warn(
    file_cr,
    file_dl,
    message_lines,
):

    file_cr = _get_cr_file_or_default(file_cr)

    if is_logging_enabled():

        file_dl = _get_log_file_or_default(file_dl)

    for message in message_lines:

        if message:

            if is_logging_enabled():

                _do_log(
                    file_dl,
                    severity.WARN,
                    message,
                )

            _add_eol_and_emit_to_cr_stm(
                file_cr,
                message,
            )


def warn(
    *message_lines,
    file=None,
    file_cr=None,
    file_dl=None,
):
    """
    Analogue of Ruby's `Kernel#warn()`

    Parameters
    ----------
    message : str, None
        The message to be emitted to the standard error stream (along with a new-line sequence). If `None`, nothing is emitted

    file : file-object, optional
        An object with a `write(str)` method, or `None` (or not present), in which case the default of `sys.stderr` will be used

    file_cr : file-object, optional
        An object with a `write(str)` method, or `None` (or not present), in which case the default given in `file` will be used. Used for contingent report output

    file_dl : file-object, optional
        An object with a `write(str)` method, or `None` (or not present), in which case the default given in `file` will be used. Used for diagnostic logging output

    Returns
    -------
    None
    """

    if file_cr is None:

        file_cr = file

    if file_dl is None:

        file_dl = file

    _warn(
        file_cr,
        file_dl,
        message_lines,
    )


# ############################## end of file ############################# #

