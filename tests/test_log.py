#! /usr/bin/env python3

from diagnosticism.logging import (
    enable_logging,
    log,
    set_log_filter,
)
from diagnosticism.program_name import set_program_name
from diagnosticism.severity import *

import unittest
from unittest.mock import patch

import re

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


class Logp_tester(unittest.TestCase):


    def test_logging_off(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging_enabled = True if enable_logging(False) else False

            try:

                set_program_name('myprog1')

                log(INFORMATIONAL, 'msg-1')

                self.assertEqual('', fake_stderr.getvalue())
            finally:

                enable_logging(logging_enabled)


    def test_message_as_string(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging_enabled = True if enable_logging(True) else False

            try:

                set_program_name('myprog1')

                log(INFORMATIONAL, 'msg-1')

                self.assertRegex(fake_stderr.getvalue(), r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*INFORMATIONAL.*\]: msg-1')
            finally:

                enable_logging(logging_enabled)


    def test__log__WITH_str_AND_file_PARAM(self):

        file = StringIO()

        logging_enabled = True if enable_logging(True) else False

        try:

            set_program_name('myprog3')

            log(INFORMATIONAL, 'msg-3', file=file)
        finally:

            enable_logging(logging_enabled)

        result = file.getvalue()

        self.assertRegex(result, r'^\[myprog3, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*INFORMATIONAL.*\]: msg-3')


    def test_message_as_lambda(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging_enabled = True if enable_logging(True) else False

            try:

                set_program_name('myprog1')

                log(INFORMATIONAL, lambda: 'msg-1')

                self.assertRegex(fake_stderr.getvalue(), r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*INFORMATIONAL.*\]: msg-1')
            finally:

                enable_logging(logging_enabled)


    def test_threshold_filter(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging = enable_logging(True)

            log_filter = set_log_filter(WARNING)

            try:

                set_program_name('myprog1')

                log(DEBUG0, 'msg-debug0')
                log(INFORMATIONAL, 'msg-informational')
                log(NOTICE, 'msg-notice')
                log(WARNING, 'msg-warning')
                log(FAILURE, 'msg-failure')
                log(CRITICAL, 'msg-critical')
                log(ALERT, 'msg-alert')

                r = fake_stderr.getvalue().rstrip()

                lines = re.split('[\r\n]', r)

                self.assertEqual(4, len(lines))
                self.assertRegex(lines[0], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*WARNING.*\]: msg-warning')
                self.assertRegex(lines[1], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*FAILURE.*\]: msg-failure')
                self.assertRegex(lines[2], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*CRITICAL.*\]: msg-critical')
                self.assertRegex(lines[3], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*ALERT.*\]: msg-alert')
            finally:

                set_log_filter(log_filter[0], log_filter[1])


    def test_dict_filter_others_action_False(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging = enable_logging(True)

            filter_dict = {

                WARNING: True,
                FAILURE: False,
                CRITICAL: True,
                ALERT: True,
                VIOLATION: True,
            }

            log_filter = set_log_filter(filter_dict, False)

            try:

                set_program_name('myprog1')

                log(DEBUG0, 'msg-debug0')
                log(INFORMATIONAL, 'msg-informational')
                log(NOTICE, 'msg-notice')
                log(WARNING, 'msg-warning')
                log(FAILURE, 'msg-failure')
                log(CRITICAL, 'msg-critical')
                log(ALERT, 'msg-alert')

                r = fake_stderr.getvalue().rstrip()

                lines = re.split('[\r\n]', r)

                self.assertEqual(3, len(lines))
                self.assertRegex(lines[0], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*WARNING.*\]: msg-warning')
                self.assertRegex(lines[1], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*CRITICAL.*\]: msg-critical')
                self.assertRegex(lines[2], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*ALERT.*\]: msg-alert')
            finally:

                set_log_filter(log_filter[0], log_filter[1])


    def test_dict_filter_others_action_True(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            logging = enable_logging(True)

            filter_dict = {

                WARNING: True,
                FAILURE: False,
                CRITICAL: True,
                ALERT: True,
                VIOLATION: True,
            }

            log_filter = set_log_filter(filter_dict, True)

            try:

                set_program_name('myprog1')

                log(DEBUG0, 'msg-debug0')
                log(INFORMATIONAL, 'msg-informational')
                log(NOTICE, 'msg-notice')
                log(WARNING, 'msg-warning')
                log(FAILURE, 'msg-failure')
                log(CRITICAL, 'msg-critical')
                log(ALERT, 'msg-alert')

                r = fake_stderr.getvalue().rstrip()

                lines = re.split('[\r\n]', r)

                self.assertEqual(6, len(lines))
                self.assertRegex(lines[0], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*DEBUG0.*\]: msg-debug0')
                self.assertRegex(lines[1], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*INFORMATIONAL.*\]: msg-informational')
                self.assertRegex(lines[2], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*NOTICE.*\]: msg-notice')
                self.assertRegex(lines[3], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*WARNING.*\]: msg-warning')
                self.assertRegex(lines[4], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*CRITICAL.*\]: msg-critical')
                self.assertRegex(lines[5], r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*ALERT.*\]: msg-alert')
            finally:

                set_log_filter(log_filter[0], log_filter[1])


if '__main__' == __name__:

    unittest.main()

