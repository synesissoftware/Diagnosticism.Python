
from .contingent_reporting import (
    _add_eol_and_emit_to_cr_stm,
    _get_cr_file_or_default,
    _output_lock,
)
from .logging import (
    _route_log,
    is_severity_logged,
)
from . import severity



def _warn(
    file_cr,
    file_dl,
    message_lines,
):

    file_cr = _get_cr_file_or_default(file_cr)

    for message in message_lines:

        if callable(message):

            message = message()

        if message:

            with _output_lock:

                if is_severity_logged(severity.WARN):

                    _route_log(file_dl, severity.WARN, message)

            _add_eol_and_emit_to_cr_stm(
                file_cr,
                message,
            )


def warn(
    *message_lines,
    **kwargs
):
    """
    Analogue of Ruby's `Kernel#warn()`

    Parameters
    ----------
    message_lines : list[str, callable]
        The message line(s) to be emitted to the standard error stream
        (along with a new-line sequence). A callable is invoked to obtain
        the line. If `None`, nothing is emitted

    file : file-object, optional
        An object with a `write(str)` method, or `None` (or not present), in
        which case the default of `sys.stderr` will be used

    file_cr : file-object, optional
        An object with a `write(str)` method, or `None` (or not present), in
        which case the default given in `file` will be used. Used for
        contingent report output

    file_dl : file-object, optional
        An object with a `write(str)` method, or `None` (or not present), in
        which case the default given in `file` will be used. Used for
        diagnostic logging output

    Returns
    -------
    None
    """

    file = kwargs.get('file', None)
    file_cr = kwargs.get('file_cr', None)
    file_dl = kwargs.get('file_dl', None)

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

