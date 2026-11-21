#! /usr/bin/env python3

from diagnosticism.logging import set_log_logger
from diagnosticism.program_name import set_program_name
from diagnosticism.tracing import (
    _apply_tracing_environment,
    dbg,
    enable_tracing,
    func,
    is_tracing_enabled,
    line,
    trace,
    tracefunc,
)
import inspect
import logging as stdlib_logging
import sys

from diagnosticism.internal import _basename

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

@tracefunc
def f2():

    return "f2-result"


class _ListHandler(stdlib_logging.Handler):

    def __init__(self):

        stdlib_logging.Handler.__init__(self)

        self.records = []

    def emit(self, record):

        self.records.append(record)


class Trace_tester(unittest.TestCase):

    def test__basename__WITH_WINDOWS_SEPARATOR_WHEN_WINDOWS(self):

        with patch('diagnosticism.internal._is_windows', return_value=True):

            self.assertEqual('file.py', _basename('C:\\dir\\file.py'))

        with patch('diagnosticism.internal._is_windows', return_value=False):

            self.assertEqual('C:\\dir\\file.py', _basename('C:\\dir\\file.py'))


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
                self.assertRegex(file.getvalue(), r'^\[myprog1, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*DEBUG5.*\]: f1()')
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


    def test__dbg__DOES_NOT_TRACE_file_KWARG(self):

        tracing_enabled = True if enable_tracing(True) else False

        try:

            set_program_name('myprog1')

            sink = StringIO()

            dbg(1, name='n', file=sink)

            text = sink.getvalue()

            self.assertIn('(int)=1', text)
            self.assertIn('name(str)=n', text)
            self.assertNotIn('file(', text)
        finally:

            enable_tracing(tracing_enabled)


    def test__tracefunc__WITH_TRACING_ENABLED(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            tracing_enabled = True if enable_tracing(True) else False

            try:

                set_program_name('myprog3')

                r = f2()

                self.assertEqual('f2-result', r)
                self.assertRegex(fake_stderr.getvalue(), r'^\[myprog3, \d+, \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}, .*DEBUG5.*\]: f2()')
            finally:

                enable_tracing(tracing_enabled)


    def test__tracefunc__PRESERVES_NAME_AND_DOCSTRING(self):

        def documented():
            """the doc"""

            return 1

        wrapped = tracefunc(documented)

        self.assertEqual('documented', wrapped.__name__)
        self.assertEqual('the doc', wrapped.__doc__)
        self.assertEqual(1, wrapped())


    def test__tracefunc__WITH_file_ARGUMENT(self):

        sink = StringIO()

        @tracefunc(file=sink)
        def named():

            return 2

        tracing_enabled = True if enable_tracing(True) else False

        try:

            set_program_name('myprog3')

            self.assertEqual(2, named())
            self.assertIn('named()', sink.getvalue())
        finally:

            enable_tracing(tracing_enabled)


    def test__tracefunc__STATICMETHOD_KEEPS_self_PARAMETER(self):

        sink = StringIO()

        class Box(object):

            @tracefunc(file=sink)
            @staticmethod
            def stat(self):

                return self

        tracing_enabled = True if enable_tracing(True) else False

        try:

            set_program_name('myprog3')

            self.assertEqual('token', Box.stat('token'))

            text = sink.getvalue()

            self.assertIn('self(str)=token', text)
            self.assertNotIn('Box.stat', text)
        finally:

            enable_tracing(tracing_enabled)


    if sys.version_info[0] >= 3:
        def test__asynctracefunc__RETURNS_COROUTINE(self):

            namespace = {}

            exec(
                "from diagnosticism.tracing import asynctracefunc\n"
                "@asynctracefunc\n"
                "async def f3():\n"
                "    return 'f3-result'\n",
                namespace,
            )

            tracing_enabled = True if enable_tracing(False) else False

            try:

                f3 = namespace['f3']

                self.assertTrue(inspect.iscoroutinefunction(f3))

                result = f3()

                self.assertTrue(hasattr(result, '__await__'))
                result.close()
            finally:

                enable_tracing(tracing_enabled)


    def test_ENABLE_TRACING_PREFERS_DIAGNOSTICISM_THEN_FALLS_THROUGH(self):

        previous = is_tracing_enabled()

        try:

            with patch.dict('os.environ', {
                'DIAGNOSTICISM_ENABLE_TRACING': 'yes',
                'ENABLE_TRACING': 'no',
            }):

                _apply_tracing_environment()

                self.assertTrue(is_tracing_enabled())

            with patch.dict('os.environ', {
                'DIAGNOSTICISM_ENABLE_TRACING': 'maybe',
                'ENABLE_TRACING': 'no',
            }):

                _apply_tracing_environment()

                self.assertFalse(is_tracing_enabled())
        finally:

            enable_tracing(True if previous else False)


    def test__trace__ROUTES_TO_STANDARD_LOGGER_AT_DEBUG(self):

        handler = _ListHandler()
        logger = stdlib_logging.getLogger('diagnosticism.test.trace_routes')
        logger.addHandler(handler)
        logger.setLevel(stdlib_logging.DEBUG)
        logger.propagate = False

        def f():

            trace()

        previous_tracing = enable_tracing(True)
        previous_logger = set_log_logger(logger)

        try:

            f()

            self.assertEqual([stdlib_logging.DEBUG], [r.levelno for r in handler.records])
            self.assertIn('f()', handler.records[0].getMessage())
        finally:

            set_log_logger(previous_logger)
            logger.removeHandler(handler)
            enable_tracing(previous_tracing)
