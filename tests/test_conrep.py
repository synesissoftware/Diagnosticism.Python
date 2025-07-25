#! /usr/bin/env python3

from diagnosticism.contingent_reporting import (
    abort,
    conrep,
    report,
    set_default_trailing_prompt,
)
from diagnosticism.program_name import set_program_name

import unittest
from unittest.mock import patch

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


class ConRep_tester(unittest.TestCase):


    def test_with_program_name(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            conrep('string-1', show_program_name=True)

            self.assertEqual("myprog1: string-1\n", fake_stderr.getvalue())


    def test_without_program_name(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            conrep('string-1', show_program_name=False)

            self.assertEqual("string-1\n", fake_stderr.getvalue())


class Report_tester(unittest.TestCase):


    def test_with_program_name(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            report('string-1', show_program_name=True)

            self.assertEqual("myprog1: string-1\n", fake_stderr.getvalue())


    def test_without_program_name(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            report('string-1', show_program_name=False)

            self.assertEqual("string-1\n", fake_stderr.getvalue())


    def test__report__WITH_file_PARAM_AND_show_program_name_False(self):

        file = StringIO()

        set_program_name('myprog3')

        report('string-3', file=file, show_program_name=False)

        result = file.getvalue()

        self.assertEqual("string-3\n", result)


    def test__report__WITH_file_PARAM_AND_show_program_name_True(self):

        file = StringIO()

        set_program_name('myprog4')

        report('string-4', file=file, show_program_name=True)

        result = file.getvalue()

        self.assertEqual("myprog4: string-4\n", result)


class Abort_tester(unittest.TestCase):


    def test_default(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            abort('over and out!', do_exit=False)

            self.assertEqual("myprog1: over and out!\n", fake_stderr.getvalue())


    def test_explicit_trailing_prompt(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            abort('over and out!', do_exit=False, trailing_prompt='get over yourself!')

            self.assertEqual("myprog1: over and out!; get over yourself!\n", fake_stderr.getvalue())


    def test_stock_trailing_prompt(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            abort('over and out!', do_exit=False, trailing_prompt=True)

            self.assertEqual("myprog1: over and out!; use --help for usage\n", fake_stderr.getvalue())


    def test_set_default_trailing_prompt_1(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            set_default_trailing_prompt('ok, now')

            abort('over and out!', do_exit=False, trailing_prompt=True)

            set_default_trailing_prompt(None)

            self.assertEqual("myprog1: over and out!; ok, now\n", fake_stderr.getvalue())


    def test_set_default_trailing_prompt_2(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            set_program_name('myprog1')

            set_default_trailing_prompt('ok, now')

            abort('over and out!', do_exit=False, trailing_prompt=False)

            set_default_trailing_prompt(None)

            self.assertEqual("myprog1: over and out!\n", fake_stderr.getvalue())


if '__main__' == __name__:

    unittest.main()

