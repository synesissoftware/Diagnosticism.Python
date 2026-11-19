#! /usr/bin/env python3

from diagnosticism.program_name import set_program_name
from diagnosticism.tracing import (
    enable_tracing,
    func,
    line,
    trace,
)
import sys
if sys.version_info[:2] >= (3, 9):
    from diagnosticism.tracing import (
        tracefunc,
    )

import unittest
from unittest.mock import patch


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

                self.assertEqual("f1-result", r)
                self.assertEqual("", file.getvalue())
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


    def test__trace__AT_MODULE_LEVEL_REPORTS_CALL_LINE(self):

        tracing_enabled = True if enable_tracing(True) else False

        try:

            set_program_name('myprog1')

            sink = StringIO()

            # The call is line 2, so this fails if trace() still uses co_firstlineno.
            exec("\ntrace(file=sink)\n", {"trace": trace, "sink": sink})

            self.assertRegex(sink.getvalue(), r'<string>:2')
        finally:

            enable_tracing(tracing_enabled)


    def test__func_AND_line_FORWARD_kwargs(self):

        with patch('diagnosticism.tracing._flf', return_value=['a.py', 3, 'g']) as flf:

            func(basename=True)
            line(basename=True)

        self.assertTrue(flf.call_args_list[0].kwargs.get('basename'))
        self.assertTrue(flf.call_args_list[1].kwargs.get('basename'))


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
