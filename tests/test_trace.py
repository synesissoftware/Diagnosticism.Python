#! /usr/bin/env python3

from diagnosticism.program_name import set_program_name
from diagnosticism.tracing import (
    enable_tracing,
    trace,
)
import sys
if sys.version_info[:2] >= (3, 9):
    from diagnosticism.tracing import (
        tracefunc,
    )

import unittest
from unittest.mock import patch

import re

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO

file = None


def f1():

    trace(file=file)

    return "f1-result"

if sys.version_info[:2] >= (3, 9):

    @tracefunc
    def f2():

        return "f2-result"
else:

    def f2():

        pass

class Trace_tester(unittest.TestCase):


    def test__trace__WITH_TRACING_DISABLED(self):

        tracing_enabled = True if enable_tracing(False) else False

        try:

            set_program_name('myprog1')

            global file

            file = StringIO()

            try:

                r = f1()

                self.assertEqual('f1-result', r)
                self.assertEqual('', file.getvalue())
            finally:

                file = None
        finally:

            enable_tracing(tracing_enabled)


    def test__trace__WITH_TRACING_ENABLED(self):

        tracing_enabled = True if enable_tracing(True) else False

        try:

            set_program_name('myprog1')

            global file

            file = StringIO()

            try:

                r = f1()

                self.assertEqual('f1-result', r)
                self.assertRegex(file.getvalue(), r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*TRACE.*\]: f1()')
            finally:

                file = None
        finally:

            enable_tracing(tracing_enabled)


    if sys.version_info[:2] >= (3, 9):
        def test__tracefunc__WITH_TRACING_ENABLED(self):

            with patch('sys.stderr', new=StringIO()) as fake_stderr:

                tracing_enabled = True if enable_tracing(True) else False

                try:

                    set_program_name('myprog3')

                    r = f2()

                    self.assertEqual('f2-result', r)
                    self.assertRegex(fake_stderr.getvalue(), r'^\[myprog3, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*TRACE.*\]: f2()')
                finally:

                    enable_tracing(tracing_enabled)
