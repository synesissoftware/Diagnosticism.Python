
import os
import platform


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

