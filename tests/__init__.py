# This file present to deal with warnings from packager

import sys

if sys.version_info[0] < 3:

    import unittest

    try:

        import mock

        sys.modules['unittest.mock'] = mock
    except ImportError:

        pass

    if not hasattr(unittest.TestCase, 'assertRegex'):

        unittest.TestCase.assertRegex = unittest.TestCase.assertRegexpMatches
