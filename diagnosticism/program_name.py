
import os
import sys


_program_name = None


def set_program_name(name):
    """
    Sets the program name

    Parameters
    ----------
    name : str
        The string to be used for the program name

    Returns
    -------
    str
        The previous program name
    """

    global _program_name

    if name:

        _program_name = name
    else:

        _program_name = os.path.basename(sys.argv[0])

    return _program_name


def get_program_name():
    """
    Gets the program name
    """

    return _program_name


# initialise the program name
set_program_name(None)


# ############################## end of file ############################# #

