
import os
import sys

_program_name = None

def set_program_name(name):

    global _program_name

    if name:

        _program_name = name
    else:

        _program_name = os.path.basename(sys.argv[0])

    return _program_name

def get_program_name():

    return _program_name

set_program_name(None)

