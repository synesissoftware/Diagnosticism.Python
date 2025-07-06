#! /usr/bin/env python3

from diagnosticism.severity import *

import unittest
from unittest.mock import patch

import re
import sys

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


INTEGER_LEVELS = [ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, ]

NAMED_LEVELS = {

    "Warn"          :   WARNING,
    "Warning"       :   WARNING,
    "WARN"          :   WARNING,
    "WARNING"       :   WARNING,
    "warn"          :   WARNING,
    "warning"       :   WARNING,
}


class ParseSeverity_tester(unittest.TestCase):


    def test_integer_levels_as_int(self):

        for i in INTEGER_LEVELS:

            expected = i
            actual = parse_verbosity(i)

            self.assertEqual(expected, actual)


    def test_integer_levels_as_str(self):

        for i in INTEGER_LEVELS:

            expected = i
            actual = parse_verbosity(str(i))

            self.assertEqual(expected, actual)


    def test_integer_levels_as_str_with_padding(self):

        for i in INTEGER_LEVELS:

            expected = i
            actual = parse_verbosity("\t%d " % (i))

            self.assertEqual(expected, actual)


    def test_named_levels(self):

        for (s, l) in NAMED_LEVELS.items():

            expected = l
            actual = parse_verbosity(s)

            self.assertEqual(expected, actual)


    def test_named_levels_with_padding(self):

        for (s, l) in NAMED_LEVELS.items():

            expected = l
            actual = parse_verbosity("\t%s " % (s))

            self.assertEqual(expected, actual)

