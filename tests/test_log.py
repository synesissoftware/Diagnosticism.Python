#! /usr/bin/env python

from diagnosticism.log import log, enable_logging
from diagnosticism.severity import INFORMATIONAL

import unittest
from unittest.mock import patch

import diagnosticism

import re

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


class Logp_tester(unittest.TestCase):

    def test_message_as_string(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging = enable_logging(True)

            try:

                diagnosticism.set_program_name('myprog1')

                log(INFORMATIONAL, 'msg-1')

                self.assertRegex(fake_stderr.getvalue(), r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*INFORMATIONAL.*\]: msg-1')
            finally:

                enable_logging(logging)

    def test_message_as_lambda(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging = enable_logging(True)

            try:

                diagnosticism.set_program_name('myprog1')

                log(INFORMATIONAL, lambda: 'msg-1')

                self.assertRegex(fake_stderr.getvalue(), r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*INFORMATIONAL.*\]: msg-1')
            finally:

                enable_logging(logging)

if '__main__' == __name__:

    unittest.main()



