#! /usr/bin/env python3

# ######################################################################## #
# File:     tests/test_warn.py
#
# Purpose:  Unit-testing of `warn()`.
#
# Created:  25th July 2025
# Updated:  25th July 2025
#
# Copyright (c) Matthew Wilson, Synesis Information Systems Pty Ltd
# All rights reserved
#
# ######################################################################## #


from diagnosticism.logging import (
    enable_logging,
)
from diagnosticism.warning import (
    warn,
)
from diagnosticism.program_name import (
    set_program_name,
)

import re
import unittest
from unittest.mock import patch

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


class Warn_tester(unittest.TestCase):


    def test__warn__WITH_PROGRAM_NAME_AND_LOGGING_DISABLED(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            logging_enabled = True if enable_logging(False) else False

            try:

                warn('warning-1')
            finally:

                enable_logging(logging_enabled)

            result = fake_stderr.getvalue()

            self.assertEqual("warning-1\n", result)


    def test__warn__WITH_PROGRAM_NAME_AND_LOGGING_ENSABLED(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog2')

            logging_enabled = True if enable_logging(True) else False

            try:

                warn('warning-2')
            finally:

                enable_logging(logging_enabled)

            result = fake_stderr.getvalue()

            regex = r"^\[myprog2,\s*\d+,\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}, WARNING]: warning-2\nwarning-2\n$"

            self.assertRegex(result, regex)


    def test__warn__WITH_file_PARAM_AND_LOGGING_DISABLED(self):

        file = StringIO()

        set_program_name('myprog3')

        logging_enabled = True if enable_logging(False) else False

        try:

            warn('warning-3', file=file)
        finally:

            enable_logging(logging_enabled)

        result = file.getvalue()

        self.assertEqual("warning-3\n", result)


    def test__warn__WITH_file_PARAM_AND_LOGGING_ENABLED(self):

        file = StringIO()

        set_program_name('myprog4')

        logging_enabled = True if enable_logging(True) else False

        try:

            warn('warning-4', file=file)
        finally:

            enable_logging(logging_enabled)

        result = file.getvalue()

        regex = r"^\[myprog4,\s*\d+,\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}, WARNING]: warning-4\nwarning-4\n$"

        self.assertRegex(result, regex)


    def test__warn__WITH_file_cr_PARAM_AND_file_dl_PARAM_AND_LOGGING_ENABLED(self):

        file_cr = StringIO()
        file_dl = StringIO()

        set_program_name('myprog4')

        logging_enabled = True if enable_logging(True) else False

        try:

            warn('warning-4', file_cr=file_cr, file_dl=file_dl)
        finally:

            enable_logging(logging_enabled)

        result_cr = file_cr.getvalue()
        result_dl = file_dl.getvalue()

        regex = r"^\[myprog4,\s*\d+,\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}, WARNING]: warning-4\n$"

        self.assertEqual("warning-4\n", result_cr)
        self.assertRegex(result_dl, regex)



    def test__warn__WITH_file_PARAM_AND_file_dl_PARAM_AND_LOGGING_ENABLED(self):

        file = StringIO()
        file_dl = StringIO()

        set_program_name('myprog4')

        logging_enabled = True if enable_logging(True) else False

        try:

            warn('warning-4', file=file, file_dl=file_dl)
        finally:

            enable_logging(logging_enabled)

        result = file.getvalue()
        result_dl = file_dl.getvalue()

        regex = r"^\[myprog4,\s*\d+,\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}, WARNING]: warning-4\n$"

        self.assertEqual("warning-4\n", result)
        self.assertRegex(result_dl, regex)


    def test__warn__WITH_MULTIPLE_LINES_WITH_PROGRAM_NAME_AND_LOGGING_DISABLED(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog5')

            logging_enabled = True if enable_logging(False) else False

            try:

                warn(
                    'warning-5a',
                    'warning-5b',
                )
            finally:

                enable_logging(logging_enabled)

            result = fake_stderr.getvalue()

            self.assertEqual("warning-5a\nwarning-5b\n", result)

