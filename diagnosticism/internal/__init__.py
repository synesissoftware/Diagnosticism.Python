
import os
import platform
import sys


TRUE_STRINGS    =   [
    'true',
    'True',
    'TRUE',
    'on',
    'On',
    'ON',
    'yes',
    'Yes',
    'YES',
    '1',
]

FALSE_STRINGS   =   [
    'false',
    'False',
    'FALSE',
    'off',
    'Off',
    'OFF',
    'no',
    'No',
    'NO',
    '0',
]

TRUE_STRINGS_lower  =   [
    'true',
    'on',
    'yes',
    '1',
]

FALSE_STRINGS_lower =   [
    'false',
    'off',
    'no',
    '0',
]


def _is_windows():
    """
    Obtains whether the operating system is a flavour of Windows.

    Returns
    -------
    bool
    """

    if os.name.lower() == 'nt':

        return True

    return False


def _is_windows_11_or_later():
    """
    Obtains whether the operating system is a flavour of Windows that is
    11 or later.

    Returns
    -------
    bool
    """

    if not _is_windows():

        return False

    from platform import release as platform_release
    from platform import version as platform_version

    release = platform_release()

    try:

        release_i = int(release)

        if release_i < 10:

            return False
    except ValueError:

        return False

    version = platform_version().split('.')

    if len(version) < 3:

        return False

    try:

        version_major   =   int(version[0])
        version_minor   =   int(version[1])
        version_patch   =   int(version[2])

        if version_major > 10:

            return True

        if version_major < 10:

            return False

        if version_minor > 0:

            return True

        if version_patch >= 22000:

            return True

    except ValueError:

        return False


def _basename(path):
    """
    Obtains the basename form of the path.

    Returns
    -------
    str
    """

    ix_last_slash   =   path.rfind('/')

    if _is_windows():

        ix_last_bslash  =   path.rfind('\\')

        if ix_last_bslash > ix_last_slash:

            ix_last_slash = ix_last_bslash

    return path[ix_last_slash + 1:]


def _str2bool(s, default_value=None):
    """
    Converts a string to a boolean, by consideration of the human-readable
    intention of the string. For example,

    Returns
    -------
    True | False | None
    """

    if s in TRUE_STRINGS:

        return True


    if s in FALSE_STRINGS:

        return False


    s = s.trim().lower()


    if s in TRUE_STRINGS_lower:

        return True


    if s in FALSE_STRINGS_lower:

        return False


    return default_value


def _bool_from_env(args, fn_name):

    if len(args) == 1:

        v = args[0]

        if not isinstance(v, bool):

            raise TypeError("`%s()` argument must be `True` or `False`; type `%s` provided" % (fn_name, type(v)))

        return v

    if len(args) == 2:

        def_val =   args[1]

        if isinstance(args[0], (list, tuple)):

            ev_names    =   args[0]
        else:

            ev_names    =   [ args[0] ]

        for ev_name in ev_names:

            if ev_name in os.environ:

                ev_val = os.environ[ev_name]

                return _str2bool(ev_val, def_val)

        if not isinstance(def_val, bool):

            raise TypeError("`%s()` argument must be `True` or `False`; type `%s` provided" % (fn_name, type(def_val)))

        return def_val

    raise TypeError("`%s()` takes 1 or 2 arguments" % fn_name)


def _is_python_2_7_or_later():

    return sys.version_info[:2] >= (2, 7)


def _is_python_3_0_or_later():

    return sys.version_info[:2] >= (3, 0)


def _is_python_3_9_or_later():

    return sys.version_info[:2] >= (3, 9)


# ############################## end of file ############################# #

