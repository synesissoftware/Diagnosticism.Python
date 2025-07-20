
from .contingent_reporting import _add_eol_and_emit_to_cr_stm
from .logging import (
    do_log,
    is_logging_enabled,
)
from . import severity

from .internal import (
    _is_python_2_7_or_later,
)


def _warn(message):

    if message:

        if is_logging_enabled():

            do_log(severity.WARN, message)

        _add_eol_and_emit_to_cr_stm(message)



if _is_python_2_7_or_later():

    def warn(
        message,
        **kwargs,
    ):
        """
        Analogue of Ruby's `Kernel#warn()`

        Parameters
        ----------
        message : str, None
            The message to be emitted to the standard error stream (along with a new-line sequence). If `None`, nothing is emitted

        Returns
        -------
        None
        """

        _warn(message)
else:

    def warn(
        message,
    ):
        """
        Analogue of Ruby's `Kernel#warn()`

        Parameters
        ----------
        message : str, None
            The message to be emitted to the standard error stream (along with a new-line sequence). If `None`, nothing is emitted

        Returns
        -------
        None
        """

        _warn(message)


# ############################## end of file ############################# #

